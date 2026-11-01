#!/usr/bin/env python3
"""Rebuild every public page from the existing, published observations.

This changes presentation only. It does not run models or regenerate run data.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

from build_campaign_explorer import build as build_home
from build_site import build_flow, render_results

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    out = ROOT / "docs"
    bundle = json.loads((out / "data/runs.json").read_text())
    render_results(bundle, out)
    for cohort in bundle["cohorts"]:
        if cohort.get("flow"):
            build_flow(ROOT / "runs" / cohort["id"], out / cohort["flow"], bundle["featured"])
    subprocess.run([sys.executable, str(ROOT / "scripts/build_level_diagram.py")], check=True)
    build_home()
    print("Built the homepage, full results, comparison flowcharts and level guide.")


if __name__ == "__main__":
    main()
