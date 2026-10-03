#!/usr/bin/env bash
# Retire the branches Wendell approved: tag each one archive/<branch> at its pinned commit, confirm the tag on GitHub,
# then remove the branch only if it still points at that commit.
#
# Usage, from a clone of six-faces-council on a computer signed in to GitHub:
#   bash council/retire_branches.sh                 retire everything in the list
#   bash council/retire_branches.sh --dry-run       say what would happen and change nothing
#   bash council/retire_branches.sh <list.tsv>      use another list
#
# Wendell chose this on the council board (archive-method, board read 15, 2026-10-03) after GitHub refused tag pushes
# from the cloud session. Transcend and include: nothing is deleted. A retired branch stays reachable as its tag, and
#   git push origin archive/<branch>:refs/heads/<branch>
# brings it back. A branch that has moved since the list was written is skipped, never removed.
set -u
here=$(cd "$(dirname "$0")" && pwd)
list="$here/census/RETIRE_2026-10-03.tsv"
dry=0
for a in "$@"; do
  case "$a" in
    --dry-run) dry=1 ;;
    *) list="$a" ;;
  esac
done
base=${RETIRE_GIT_BASE:-https://github.com/}   # tests point this at local repos
log="$PWD/retire-$(date +%Y%m%d-%H%M%S).log"
work=$(mktemp -d)
retired=0; skipped=0; failed=0

say() { echo "$*" | tee -a "$log"; }

for repo in $(grep -v '^#' "$list" | cut -f1 | sort -u); do
  url="$base$repo"
  dir="$work/$(echo "$repo" | tr / _)"
  say "== $repo"
  if ! git clone -q --bare --filter=blob:none --no-tags "$url" "$dir" 2>>"$log"; then
    say "FAILED to clone $url; nothing in this repo was touched"
    failed=$((failed + $(grep -v '^#' "$list" | awk -F'\t' -v r="$repo" '$1==r' | wc -l)))
    continue
  fi
  while IFS=$'\t' read -r r branch sha why; do
    [ "$r" = "$repo" ] || continue
    now=$(git -C "$dir" ls-remote origin "refs/heads/$branch" | cut -f1)
    if [ -z "$now" ]; then say "skip   $branch: it is already gone"; skipped=$((skipped+1)); continue; fi
    if [ "$now" != "$sha" ]; then say "skip   $branch: it moved since the list was written ($now)"; skipped=$((skipped+1)); continue; fi
    tag=$(git -C "$dir" ls-remote origin "refs/tags/archive/$branch" | cut -f1)
    if [ -n "$tag" ] && [ "$tag" != "$sha" ]; then say "skip   $branch: archive/$branch already exists at another commit"; skipped=$((skipped+1)); continue; fi
    if [ $dry = 1 ]; then say "would  $branch -> archive/$branch at ${sha:0:10}"; continue; fi
    if [ -z "$tag" ] && ! git -C "$dir" push -q origin "$sha:refs/tags/archive/$branch" 2>>"$log"; then
      say "FAILED $branch: the tag push was refused; the branch is untouched"; failed=$((failed+1)); continue
    fi
    tag=$(git -C "$dir" ls-remote origin "refs/tags/archive/$branch" | cut -f1)
    if [ "$tag" != "$sha" ]; then say "FAILED $branch: the tag did not appear; the branch is untouched"; failed=$((failed+1)); continue; fi
    if git -C "$dir" push -q --force-with-lease="refs/heads/$branch:$sha" origin ":refs/heads/$branch" 2>>"$log"; then
      say "done   $branch -> archive/$branch"; retired=$((retired+1))
    else
      say "FAILED $branch: tagged, but the branch removal was refused"; failed=$((failed+1))
    fi
  done < <(grep -v '^#' "$list")
done
rm -rf "$work"
if [ $dry = 1 ]; then say "Dry run: nothing changed."; fi
say "$retired retired, $skipped skipped, $failed failed. The log is $log"
[ $failed = 0 ]
