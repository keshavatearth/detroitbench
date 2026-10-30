#!/usr/bin/env python3
"""Audit graph references against the optional, local upstream transcript.

Source-key resolution is a provenance check, not a claim of complete game
coverage or proof that every condition has been reconstructed correctly.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from detroitbench.campaign import canonical_hash, load_chapters, validate_chapters


def resolve_key(corpus: dict, key: str):
    value = corpus
    for component in key.split("."):
        value = value[component]
    return value


def audit(source_root: Path | None = None) -> dict:
    chapters = load_chapters()
    source_root = source_root or ROOT / "source"
    translation = source_root / "public/i18n/en.json"
    corpus = json.loads(translation.read_text()) if translation.exists() else None
    errors = validate_chapters(chapters)
    rows = []
    refs_all: set[str] = set()
    for chapter in chapters:
        refs: set[str] = set()
        missing = []
        unsourced = []
        for node_id, node in chapter["nodes"].items():
            for part in [node, *node.get("actions", [])]:
                source_refs = part.get("source_refs", [])
                refs.update(source_refs)
                if part.get("text", "").strip() and not source_refs:
                    unsourced.append(node_id + (":" + part["id"] if "id" in part else ""))
        resolved = 0
        keyed = sorted(ref for ref in refs if re.match(r"^(X[0-9A-Z]+|GUI|MENU|THOUGHTS)\.", ref))
        if corpus is not None:
            for ref in keyed:
                try:
                    resolve_key(corpus, ref)
                    resolved += 1
                except (KeyError, TypeError):
                    missing.append(ref)
                    errors.append(f"chapter {chapter['number']}: missing translation key {ref}")
        rows.append({"number": chapter["number"], "id": chapter["id"], "title": chapter["title"],
            "nodes": len(chapter["nodes"]), "choice_nodes": sum(n["kind"] == "choice" for n in chapter["nodes"].values()),
            "actions": sum(len(n.get("actions", [])) for n in chapter["nodes"].values()),
            "end_nodes": sum(n["kind"] == "end" for n in chapter["nodes"].values()),
            "unique_translation_keys": len(keyed), "resolved_translation_keys": resolved if corpus is not None else None,
            "missing_translation_keys": missing, "text_without_direct_source_refs": unsourced,
            "fidelity": chapter.get("fidelity", {})})
        refs_all.update(keyed)
    total_nodes = sum(row["nodes"] for row in rows)
    total_actions = sum(row["actions"] for row in rows)
    source_status = "verified" if corpus is not None else "not-available"
    summary = (f"{len(chapters)} chapters; {total_nodes} authored nodes and {total_actions} actions in the new JSON graph. "
               f"{len(refs_all)} unique translation keys " + ("resolved against the pinned local corpus." if corpus is not None else "not checked: local corpus is unavailable."))
    return {"schema": "detroitbench-campaign-audit-1", "ok": not errors, "summary": summary,
        "graph_sha256": canonical_hash(chapters), "source_status": source_status,
        "translation_sha256": hashlib.sha256(translation.read_bytes()).hexdigest() if corpus is not None else None,
        "coverage_claim": "Structural graph checks and translation-key existence only. Not exhaustive game coverage, dialogue-order verification, or empirical model evidence.",
        "chapters": rows, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the JSON audit to this path")
    parser.add_argument("--require-source", action="store_true", help="Fail when the local upstream transcript is unavailable")
    args = parser.parse_args()
    result = audit()
    if args.require_source and result["source_status"] != "verified":
        result["ok"] = False
        result["errors"].append("The upstream transcript is required for this audit")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(result["summary"])
    for error in result["errors"]:
        print(error, file=sys.stderr)
    return int(not result["ok"])


if __name__ == "__main__":
    raise SystemExit(main())
