"""Superseded by board/pull.py (pickup-pull-model, 2026-10-07), whose report mode prints the same list and which records
it. Kept because older routine prompts still name it.

List the answers Wendell saved on the board that main has not recorded.

The daily run of 2026-10-04 found 23 saves no session had read (council/research/2026-10-04-saved-but-never-recorded.md);
two of them should have merged pull requests. sync_board.py brings the page's rows to main but never reads the saves.
Wendell stood dy-2026-10-04-open, which proposed this check at the start of every board read.

Save the store first with the ArtifactData tool, once per collection:
  action list, collection positions (then questions, terms), query {"limit": 1000}, out_dir <dir>
Then: python3 board/unrecorded.py <dir>
It prints one line per saved answer with no resolved entry in board/board_data.json, and exits 1 if there are any.
"""
import json, sys
from pathlib import Path

KINDS = ("positions", "questions", "terms", "causes")


def answer(kind, doc):
    if kind == "positions":
        return doc.get("status", "")
    if kind == "terms":
        return doc.get("action", "")
    return doc.get("choice") or ("steer" if doc.get("steer") else "")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    store = Path(sys.argv[1])
    data = json.loads((Path(__file__).parent / "board_data.json").read_text(encoding="utf-8"))
    resolved = data.get("resolved", {})
    found = []
    for kind in KINDS:
        for f in sorted((store / kind).glob("*.json")):
            doc = json.loads(f.read_text(encoding="utf-8"))
            if f.stem in resolved.get(kind, {}) or not (answer(kind, doc) or doc.get("steer")):
                continue
            found.append((doc.get("savedAt", ""), kind, f.stem, answer(kind, doc), doc.get("via", "")))
    for saved, kind, rid, ans, via in sorted(found):
        print(f"{saved}  {kind:<9} {rid}  {ans or 'steer'}" + (f"  ({via})" if via else ""))
    print(f"{len(found)} saved answers not recorded" if found else "every saved answer is recorded")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
