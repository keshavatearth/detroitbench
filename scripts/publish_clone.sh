#!/bin/sh
# Prepare a publishable copy of this repository: a fresh clone with the
# upstream transcript app (source/) removed from every commit. Nothing is pushed.
#
#   scripts/publish_clone.sh [target-dir]      # default: ../detroitbench-public
#
# Afterwards, review the clone, then (manually):
#   cd ../detroitbench-public
#   gh repo create keshavatearth/detroitbench --public --source . --push
#   gh api -X POST repos/keshavatearth/detroitbench/pages -f source[branch]=main -f source[path]=/docs
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
TARGET=${1:-"$ROOT/../detroitbench-public"}
command -v git-filter-repo >/dev/null || { echo "git-filter-repo is required (brew install git-filter-repo)"; exit 1; }
[ -e "$TARGET" ] && { echo "target exists: $TARGET"; exit 1; }
git clone --quiet --no-local "$ROOT" "$TARGET"
cd "$TARGET"
git filter-repo --quiet --path source --invert-paths --force
git remote remove origin 2>/dev/null || true
echo "history rewritten: $(git rev-list --count HEAD) commits, source/ removed"
if git log --all --name-only --format= | grep -q '^source/'; then echo "ERROR: source/ still present"; exit 1; fi
if grep -rIl "/Users/" --exclude-dir=.git . | head -1 | grep -q .; then echo "WARNING: private paths remain:"; grep -rIl "/Users/" --exclude-dir=.git . | head; fi
du -sh .git
echo "ready: $TARGET (not pushed)"
