"""Push to bars-engine from a cloud session, which has no GitHub credential of its own.

The connected GitHub app can read bars-engine and commit through the API, but a `git push` needs a credential inside
this VM and the app's is not handed to it: git answers "could not read Username for 'https://github.com'". So the
credential is a project secret. Add `BARS_ENGINE_TOKEN` in this project's Settings -> Secrets: a classic token with the
`public_repo` scope (bars-engine is public, and a fine-grained token cannot be scoped to a repository owned by another
user's account, so its repository picker comes up empty). Every shell in the project reads that file, so no session
needs to be told the value, and nothing here writes it anywhere: the helper below reads the variable when git asks for
it.

  python3 council/tools/bars_git.py check          # is there a token, and does the remote answer
  python3 council/tools/bars_git.py setup          # point this checkout's credential helper at the variable
  python3 council/tools/bars_git.py push BRANCH    # push HEAD to BRANCH on bars-engine

The checkout is the one `blender_here.py bars` makes (`$BLENDER_HERE_ROOT/bars-engine`); `BARS_CHECKOUT` points this at
another. Pushing is only ever done when asked: this tool never pushes on its own.
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

TOKEN_VAR = "BARS_ENGINE_TOKEN"
REMOTE = "https://github.com/johnair01/bars-engine"
ROOT = Path(os.environ.get("BLENDER_HERE_ROOT", Path.home() / "blender-here"))
CHECKOUT = Path(os.environ.get("BARS_CHECKOUT", ROOT / "bars-engine"))
HELPER = ('!f() { if [ "$1" = get ]; then echo username=x-access-token; '
          'echo "password=${%s}"; fi; }; f' % TOKEN_VAR)

MISSING = (f"no {TOKEN_VAR} in this session's environment. Add it in Settings -> Secrets as a classic token with the "
           f"public_repo scope, then run this again in a new shell.")


def say(msg):
    print(msg, flush=True)


def token():
    return os.environ.get(TOKEN_VAR, "").strip()


def git(*args, check=False):
    return subprocess.run(["git", "-C", str(CHECKOUT), *args], capture_output=True, text=True, check=check,
                          env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})


def check():
    """Whether a push could work: the checkout, the token, the helper, and the remote with the token applied."""
    have_token = bool(token())
    report = {"checkout": str(CHECKOUT), "checkout_present": (CHECKOUT / ".git").exists(),
              "token_var": TOKEN_VAR, "token_present": have_token,
              "remote": git("remote", "get-url", "origin").stdout.strip() or REMOTE}
    ready = False
    if not report["checkout_present"]:
        report["why"] = "no checkout; run: python3 council/tools/blender_here.py bars"
    elif not have_token:
        report["why"] = MISSING
    else:
        report["helper"] = git("config", "--local", "--get", "credential.helper").stdout.strip() or None
        probe = subprocess.run(["git", "ls-remote", "--heads", REMOTE, "main"], capture_output=True, text=True,
                               env={**os.environ, "GIT_TERMINAL_PROMPT": "0",
                                    "GIT_ASKPASS": "true", "GIT_CONFIG_COUNT": "1",
                                    "GIT_CONFIG_KEY_0": "credential.helper",
                                    "GIT_CONFIG_VALUE_0": HELPER})
        report["remote_answers"] = ready = probe.returncode == 0
        if probe.returncode:
            report["why"] = (probe.stderr or probe.stdout).strip()[-300:]
    say(json.dumps(report, indent=1))
    return 0 if ready else 1  # zero means a push from here would work now


def setup():
    if not (CHECKOUT / ".git").exists():
        raise SystemExit(f"no checkout at {CHECKOUT}; run: python3 council/tools/blender_here.py bars")
    if not token():
        raise SystemExit(MISSING)
    # the helper, not the secret: .git/config ends up naming the variable and nothing else
    subprocess.run(["git", "-C", str(CHECKOUT), "config", "--local", "credential.helper", HELPER], check=True)
    say(f"{CHECKOUT}: credential helper reads ${TOKEN_VAR} when git asks (no secret written)")
    return 0


def push(branch):
    if not token():
        raise SystemExit(MISSING)
    status = git("status", "--porcelain").stdout.strip()
    if status:
        say(f"note: {len(status.splitlines())} uncommitted path(s) stay behind; commit first if they belong in it")
    setup()
    run = subprocess.run(["git", "-C", str(CHECKOUT), "push", "-u", "origin", f"HEAD:{branch}"],
                         capture_output=True, text=True,
                         env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    say((run.stderr or run.stdout).strip()[-600:])
    if run.returncode:
        return 1
    say(f"pushed {CHECKOUT} HEAD to {REMOTE} {branch}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Push to bars-engine with the project's token.")
    ap.add_argument("command", choices=("check", "setup", "push"))
    ap.add_argument("branch", nargs="?", default="")
    a = ap.parse_args(argv)
    if a.command == "check":
        return check()
    if a.command == "setup":
        return setup()
    if not a.branch:
        raise SystemExit("push needs a branch name, e.g. push agent/j7-r1-checks")
    return push(a.branch)


if __name__ == "__main__":
    sys.exit(main())
