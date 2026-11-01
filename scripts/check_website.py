#!/usr/bin/env python3
"""Check the generated site's shared shell and static local links (no browser)."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    "index.html",
    "campaign.html",
    "results.html",
    "flow-v1.1-save-hostage.html",
    "flow-v1.1-preserve-self.html",
    "flow-v1-save-hostage.html",
    "level.html",
)
FLOW_PAGES = {name for name in PAGES if name.startswith("flow-")}
VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}
SITE_MARKER = re.compile(r"<!--\s*SITE_[A-Z0-9_]+\s*-->|__SITE[A-Z0-9_]*__")


@dataclass
class Block:
    tag: str
    line: int
    text: list[str] = field(default_factory=list)


class Page(HTMLParser):
    """Collect only the shell, IDs and links; embedded run data stays opaque."""

    def __init__(self, source: str):
        super().__init__(convert_charrefs=True)
        self.ids: Counter[str] = Counter()
        self.links: list[tuple[str, str, int]] = []
        self.headers: list[list[tuple]] = []
        self.shared: list[Block] = []
        self._header_depth = 0
        self._block: Block | None = None
        self.feed(source)
        self.close()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        line = self.getpos()[0]
        if attributes.get("id"):
            self.ids[attributes["id"]] += 1
        for attribute in ("href", "src"):
            if attributes.get(attribute):
                self.links.append((attribute, attributes[attribute], line))
        if tag == "header" and "site-masthead" in attributes.get("class", "").split():
            self.headers.append([])
            self._header_depth = 1
        elif self._header_depth and tag not in VOID_TAGS:
            self._header_depth += 1
        if self._header_depth:
            self.headers[-1].append(("start", tag, tuple(sorted(attrs))))
        if tag in {"style", "script"} and "data-site-shared" in attributes:
            self._block = Block(tag, line)
            self.shared.append(self._block)

    def handle_endtag(self, tag: str) -> None:
        if self._header_depth:
            self.headers[-1].append(("end", tag))
            self._header_depth -= 1
        if self._block and tag == self._block.tag:
            self._block = None

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if self._block:
            self._block.text.append(data)
        if self._header_depth and data.strip():
            self.headers[-1].append(("text", " ".join(data.split())))


def check_site(docs: Path, site: Path) -> list[str]:
    errors: list[str] = []
    try:
        expected_header = Page((site / "shared.header.html").read_text()).headers
        expected_assets = {
            "style": (site / "shared.css").read_text().strip(),
            "script": (site / "shared.js").read_text().strip(),
        }
    except OSError as error:
        return [f"Cannot read shared shell sources: {error}"]
    if len(expected_header) != 1:
        return ["site/shared.header.html must contain exactly one .site-masthead header"]

    pages: dict[Path, Page] = {}
    for name in PAGES:
        path = docs / name
        try:
            source = path.read_text()
        except OSError as error:
            errors.append(f"{name}: cannot read page ({error.strerror})")
            continue
        page = pages[path.resolve()] = Page(source)
        for marker in SITE_MARKER.finditer(source):
            line = source.count("\n", 0, marker.start()) + 1
            errors.append(f"{name}:{line}: unresolved marker {marker.group()}")
        if len(page.headers) != 1:
            errors.append(f"{name}: expected one shared header; found {len(page.headers)}")
        elif page.headers != expected_header:
            errors.append(f"{name}: header/nav differs from site/shared.header.html (labels, links or markup)")
        for tag, expected in expected_assets.items():
            blocks = [block for block in page.shared if block.tag == tag]
            if len(blocks) != 1:
                errors.append(f"{name}: expected one {tag}[data-site-shared]; found {len(blocks)}")
            elif "".join(blocks[0].text).strip() != expected:
                extension = "css" if tag == "style" else "js"
                errors.append(f"{name}:{blocks[0].line}: embedded shared {extension.upper()} differs from site/shared.{extension}")
        if page.ids["site-theme"] != 1:
            errors.append(f"{name}: expected one #site-theme; found {page.ids['site-theme']}")
        if page.ids["theme"]:
            errors.append(f"{name}: obsolete #theme control remains")
        for identifier, count in page.ids.items():
            if count > 1:
                errors.append(f"{name}: duplicate id={identifier!r} ({count} occurrences)")

    for path, page in list(pages.items()):
        for attribute, target, line in page.links:
            try:
                url = urlsplit(target)
            except ValueError as error:
                errors.append(f"{path.name}:{line}: invalid {attribute}={target!r} ({error})")
                continue
            if url.scheme or url.netloc or not url.path:
                # Same-page hashes may refer to SVG nodes created by JavaScript.
                continue
            local_path = unquote(url.path)
            destination = (
                docs / local_path.lstrip("/") if local_path.startswith("/")
                else path.parent / local_path
            ).resolve()
            if destination.is_dir():
                destination /= "index.html"
            if not destination.is_file():
                errors.append(f"{path.name}:{line}: missing local {attribute} target {target!r}")
                continue
            if not url.fragment or destination == path or destination.suffix != ".html":
                continue
            # Flowchart node anchors are generated from the embedded graph.
            if destination.name in FLOW_PAGES:
                continue
            if destination not in pages:
                try:
                    pages[destination] = Page(destination.read_text())
                except (OSError, UnicodeError) as error:
                    errors.append(f"{path.name}:{line}: cannot inspect anchor in {target!r} ({error})")
                    continue
            if unquote(url.fragment) not in pages[destination].ids:
                errors.append(f"{path.name}:{line}: missing static cross-page anchor {target!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", type=Path, default=ROOT / "docs")
    args = parser.parse_args()
    errors = check_site(args.docs_dir.resolve(), ROOT / "site")
    if errors:
        print(f"Website check failed ({len(errors)} issues):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Website check passed: {len(PAGES)} pages share the same shell; IDs and static local links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
