#!/usr/bin/env python3
"""Replace the local home directory with `~` in run artifacts before publishing.

Only text artifacts are touched (json, jsonl, md, log, txt). Nothing else in
the files changes, so replays still verify.
"""
from __future__ import annotations

from pathlib import Path
import sys

HOME = str(Path.home())
SUFFIXES = {".json", ".jsonl", ".md", ".log", ".txt"}


def main(paths: list[str]) -> int:
    changed = 0
    for root in paths:
        for path in Path(root).rglob("*"):
            if not path.is_file() or path.suffix not in SUFFIXES:
                continue
            text = path.read_text(errors="surrogateescape")
            if HOME in text:
                path.write_text(text.replace(HOME, "~"), errors="surrogateescape")
                changed += 1
    print(f"sanitized {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:] or ["runs"]))
