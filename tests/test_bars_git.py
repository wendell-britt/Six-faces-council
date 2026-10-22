"""council/tools/bars_git.py: pushing to bars-engine needs a credential this VM does not otherwise have.

The push itself needs the network and the token, so these tests keep the parts that can be wrong without either: the
variable name, the helper never holding a secret, and the refusal being useful when the token is absent.
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRIVER = ROOT / "council" / "tools" / "bars_git.py"

sys.path.insert(0, str(DRIVER.parent))
import bars_git  # noqa: E402


def test_the_helper_names_the_variable_and_holds_no_secret():
    assert bars_git.TOKEN_VAR == "BARS_ENGINE_TOKEN"
    assert f"${{{bars_git.TOKEN_VAR}:-" in bars_git.HELPER  # the variable first, then the file
    assert str(bars_git.TOKEN_FILE) in bars_git.HELPER
    assert "password=" in bars_git.HELPER and bars_git.HELPER.count("username=") == 1
    # nothing that looks like a token value: no long hex or ghp_/github_pat_ literals
    assert "ghp_" not in bars_git.HELPER and "github_pat_" not in bars_git.HELPER


def test_without_the_token_it_says_where_to_put_it(tmp_path):
    env = dict(os.environ, BLENDER_HERE_ROOT=str(tmp_path), BARS_CHECKOUT=str(tmp_path / "bars-engine"),
               BARS_TOKEN_FILE=str(tmp_path / "no-such-token"))
    env.pop(bars_git.TOKEN_VAR, None)
    run = subprocess.run([sys.executable, str(DRIVER), "check"], capture_output=True, text=True, env=env)
    assert run.returncode == 1  # zero would mean a push from here would work now
    assert "blender_here.py bars" in run.stdout  # the checkout comes first, before the token


def test_a_checkout_without_the_token_names_the_secret(tmp_path):
    checkout = tmp_path / "bars-engine"
    subprocess.run(["git", "init", "-q", str(checkout)], check=True)
    env = dict(os.environ, BARS_CHECKOUT=str(checkout), BLENDER_HERE_ROOT=str(tmp_path),
               BARS_TOKEN_FILE=str(tmp_path / "no-such-token"))
    env.pop(bars_git.TOKEN_VAR, None)
    run = subprocess.run([sys.executable, str(DRIVER), "check"], capture_output=True, text=True, env=env)
    assert run.returncode == 1
    assert "no-such-token" in run.stdout and "public_repo" in run.stdout


def test_setup_refuses_without_a_token_and_writes_nothing(tmp_path):
    checkout = tmp_path / "bars-engine"
    (checkout / ".git").mkdir(parents=True)
    env = dict(os.environ, BARS_CHECKOUT=str(checkout), BLENDER_HERE_ROOT=str(tmp_path),
               BARS_TOKEN_FILE=str(tmp_path / "no-such-token"))
    env.pop(bars_git.TOKEN_VAR, None)
    run = subprocess.run([sys.executable, str(DRIVER), "setup"], capture_output=True, text=True, env=env)
    assert run.returncode != 0
    assert "no-such-token" in run.stderr and "public_repo" in run.stderr


def test_setup_points_the_checkout_at_the_variable(tmp_path):
    checkout = tmp_path / "bars-engine"
    subprocess.run(["git", "init", "-q", str(checkout)], check=True)
    env = dict(os.environ, BARS_CHECKOUT=str(checkout), BLENDER_HERE_ROOT=str(tmp_path),
               BARS_ENGINE_TOKEN="not-a-real-token")
    run = subprocess.run([sys.executable, str(DRIVER), "setup"], capture_output=True, text=True, env=env)
    assert run.returncode == 0, run.stderr
    helper = subprocess.run(["git", "-C", str(checkout), "config", "--local", "--get", "credential.helper"],
                            capture_output=True, text=True).stdout
    assert bars_git.TOKEN_VAR in helper
    assert "not-a-real-token" not in helper  # the value never lands in .git/config
    assert "not-a-real-token" not in run.stdout


def test_push_needs_a_branch_name(tmp_path):
    env = dict(os.environ, BARS_CHECKOUT=str(tmp_path), BLENDER_HERE_ROOT=str(tmp_path))
    run = subprocess.run([sys.executable, str(DRIVER), "push"], capture_output=True, text=True, env=env)
    assert run.returncode != 0
    assert "branch name" in (run.stderr or run.stdout)


def test_push_puts_head_on_the_named_branch(tmp_path):
    """End to end against a local remote: the refspec, the setup, and the exit code, with no GitHub needed."""
    bare = tmp_path / "remote.git"
    subprocess.run(["git", "init", "--bare", "-q", str(bare)], check=True)
    checkout = tmp_path / "bars-engine"
    subprocess.run(["git", "init", "-q", str(checkout)], check=True)
    subprocess.run(["git", "-C", str(checkout), "remote", "add", "origin", str(bare)], check=True)
    (checkout / "a.txt").write_text("one line\n")
    subprocess.run(["git", "-C", str(checkout), "add", "a.txt"], check=True)
    subprocess.run(["git", "-C", str(checkout), "-c", "user.name=t", "-c", "user.email=t@example.com",
                    "commit", "-qm", "one"], check=True)
    env = dict(os.environ, BARS_CHECKOUT=str(checkout), BLENDER_HERE_ROOT=str(tmp_path), BARS_ENGINE_TOKEN="fake")
    run = subprocess.run([sys.executable, str(DRIVER), "push", "agent/test-branch"], capture_output=True, text=True,
                         env=env)
    assert run.returncode == 0, run.stdout + run.stderr
    refs = subprocess.run(["git", "-C", str(bare), "branch", "--list"], capture_output=True, text=True).stdout
    assert "agent/test-branch" in refs


def test_a_token_file_is_read_and_never_printed(tmp_path):
    token_file = tmp_path / "bars-engine-token"
    token_file.write_text("a-fake-token-value\n", encoding="utf-8")
    checkout = tmp_path / "bars-engine"
    subprocess.run(["git", "init", "-q", str(checkout)], check=True)
    env = {k: v for k, v in os.environ.items() if k != "BARS_ENGINE_TOKEN"}
    env.update(BARS_CHECKOUT=str(checkout), BLENDER_HERE_ROOT=str(tmp_path), BARS_TOKEN_FILE=str(token_file))
    run = subprocess.run([sys.executable, str(DRIVER), "check"], capture_output=True, text=True, env=env)
    assert '"token_present": true' in run.stdout and '"token_from": "file"' in run.stdout
    assert "a-fake-token-value" not in run.stdout + run.stderr
    assert "a-fake-token-value" not in (checkout / ".git" / "config").read_text()


def test_install_moves_the_token_out_of_the_tree(tmp_path):
    dropped = tmp_path / "bars-token.txt"
    dropped.write_text("a-fake-token-value\n", encoding="utf-8")
    installed = tmp_path / "secrets" / "bars-engine-token"
    env = dict(os.environ, BARS_TOKEN_FILE=str(installed), BARS_CHECKOUT=str(tmp_path), BLENDER_HERE_ROOT=str(tmp_path))
    run = subprocess.run([sys.executable, str(DRIVER), "install", str(dropped)], capture_output=True, text=True, env=env)
    assert run.returncode == 0, run.stderr
    assert installed.read_text().strip() == "a-fake-token-value"
    assert oct(installed.stat().st_mode)[-3:] == "600"
    assert not dropped.exists()  # out of the tree, so a stray git add cannot reach it
    assert "a-fake-token-value" not in run.stdout + run.stderr
