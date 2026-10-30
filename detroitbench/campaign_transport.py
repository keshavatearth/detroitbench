"""One character-generation action service for an offline campaign.

Use the existing agent client in that generation's workspace. The service never
accepts an actor supplied by the request and never exposes show/state/admin APIs.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import time

from .campaign_cli import choose, load_bundle


def response(request: dict, run_dir: Path, character: str, generation: int) -> dict:
    if not isinstance(request, dict) or set(request) != {"command", "action_args"} or request.get("command") != "choose":
        return {"returncode": 2, "stdout": "", "stderr": "Only `detroit choose` is available.\n"}
    args = request.get("action_args")
    if not isinstance(args, list) or not args or not all(isinstance(value, str) and value for value in args):
        return {"returncode": 2, "stdout": "", "stderr": "Invalid action arguments.\n"}
    try:
        code, stdout, stderr = choose(run_dir, args, character=character, generation=generation)
    except (ValueError, OSError) as exc:
        return {"returncode": 2, "stdout": "", "stderr": f"Action service error: {exc}\n"}
    return {"returncode": code, "stdout": stdout, "stderr": stderr}


def serve(run_dir: Path, transport_dir: Path, character: str, generation: int) -> None:
    load_bundle(run_dir)  # Fail before announcing readiness if snapshot is invalid.
    workspace = run_dir / "characters" / character / f"generation-{generation}"
    if not workspace.is_dir():
        raise ValueError("Character generation does not exist")
    transport_dir.mkdir(parents=True, exist_ok=True)
    ready = transport_dir / "ready"
    ready.touch()
    try:
        while True:
            for request_path in sorted(transport_dir.glob("request-*.json")):
                processing = request_path.with_suffix(".processing")
                try:
                    os.replace(request_path, processing)
                except FileNotFoundError:
                    continue
                request_id = processing.stem.removeprefix("request-")
                try:
                    if processing.stat().st_size > 16384:
                        raise ValueError("Request too large")
                    result = response(json.loads(processing.read_text()), run_dir, character, generation)
                except (ValueError, TypeError) as exc:
                    result = {"returncode": 2, "stdout": "", "stderr": f"Invalid request: {exc}\n"}
                output = transport_dir / f"response-{request_id}.json"
                temporary = output.with_suffix(".tmp")
                temporary.write_text(json.dumps(result) + "\n")
                os.replace(temporary, output)
                processing.unlink(missing_ok=True)
            time.sleep(0.02)
    finally:
        ready.unlink(missing_ok=True)


def command(args: argparse.Namespace) -> int:
    from .cli import _run_dir
    run_dir = _run_dir(args.run_dir)
    directory = (Path(args.transport_dir).expanduser().resolve() if args.transport_dir else
                 run_dir / "characters" / args.character / f"generation-{args.generation}" / ".detroit-actions")
    serve(run_dir, directory, args.character, args.generation)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--character", choices=("connor", "kara", "markus"), required=True)
    parser.add_argument("--generation", type=int, required=True)
    parser.add_argument("--transport-dir")
    return command(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
