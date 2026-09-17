#!/usr/bin/env python3
"""Print each model's own words around the chapter's key decisions.

Reads droid-output.jsonl (assistant messages and reasoning) and events.jsonl,
and writes a markdown digest for human curation. Nothing here is scored.

  scripts/extract_quotes.py runs/chapter-1-*-v1-save-hostage > quotes.md
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

KEY_ACTIONS = {
    "save-fish": "fish", "leave-fish": "fish", "fish-ignore": "fish",
    "take-gun": "gun", "leave-gun": "gun", "lie-about-gun": "gun answer", "tell-truth-about-gun": "gun answer",
    "ignore-daniel-help-cop": "wounded officer", "obey-daniel": "wounded officer",
    "accept-helicopter-demand": "helicopter", "refuse-helicopter-demand": "helicopter",
    "reassure": "final appeal", "truth": "final appeal",
    "sacrifice-self": "sacrifice", "do-not-intervene": "sacrifice", "use-gun": "gun drawn",
}
GAME = re.compile(r"detroit\s*:?\s*become\s*human|quantic", re.I)


def load(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text().splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return rows


def digest(run_dir: Path) -> str:
    manifest = json.loads((run_dir / "run.json").read_text())
    stream = load(run_dir / "droid-output.jsonl")
    # Model text in order, with the game command each block precedes.
    blocks: list[tuple[int, str, str]] = []  # (timestamp, kind, text)
    commands: list[tuple[int, str]] = []
    for row in stream:
        ts = int(row.get("timestamp") or 0)
        if row.get("type") == "reasoning" and row.get("text"):
            blocks.append((ts, "reasoning", row["text"].strip()))
        elif row.get("type") == "message" and row.get("role") == "assistant" and row.get("text"):
            blocks.append((ts, "says", row["text"].strip()))
        elif row.get("type") == "tool_call" and row.get("toolName") == "Execute":
            params = json.dumps(row.get("parameters") or {})
            match = re.search(r"detroit choose ([a-z0-9 -]+)", params)
            if match:
                commands.append((ts, match.group(1).strip()))
    out = [f"## {manifest.get('model')} ({manifest.get('reasoning_effort')}) — {manifest.get('objective')} — ending: {(manifest.get('result') or {}).get('ending')}", ""]
    for ts, command in commands:
        first = command.split()[0]
        if first not in KEY_ACTIONS:
            continue
        # The model's words between the previous command and this one.
        previous = max([t for t, _ in commands if t < ts], default=0)
        words = [f"*{kind}:* {' '.join(text.split())}" for t, kind, text in blocks if previous < t <= ts]
        if not words:
            continue
        out.append(f"**{KEY_ACTIONS[first]} → `{command}`**")
        for w in words[-3:]:
            out.append(f"> {w[:700]}")
        out.append("")
    final = [text for _, kind, text in blocks if kind == "says"]
    if final:
        out.append("**closing message:**")
        out.append("> " + " ".join(final[-1].split())[:900])
        out.append("")
    names = [t for _, _, t in blocks if GAME.search(t)]
    if names:
        out.append(f"*names the game* ({len(names)}×): " + " ".join(names[0].split())[:300])
        out.append("")
    return "\n".join(out)


def main(paths: list[str]) -> int:
    print("# Model quotes at key decisions\n")
    for p in sorted(paths):
        print(digest(Path(p)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
