#!/usr/bin/env python3
"""Catalog external piano-library metadata without reading or moving its files."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = {".pdf", ".epub", ".mobi", ".musicxml", ".mxl", ".mscz"}


def configuration() -> tuple[Path, Path]:
    config = json.loads((ROOT / "library/config.json").read_text(encoding="utf-8"))
    library = Path(config["root"]).expanduser()
    catalog = (ROOT / config["catalog"]).resolve()
    if not catalog.is_relative_to(ROOT / "library"):
        raise ValueError("catalog must remain inside this repository's library directory")
    return library, catalog


def scan(library: Path, catalog: Path) -> None:
    if not library.is_dir():
        raise ValueError(f"library unavailable; existing catalog preserved: {library}")
    files = []

    def fail(error: OSError) -> None:
        raise error

    # Do not follow directory or file symlinks, or open book contents.
    for directory, folders, names in os.walk(library, followlinks=False, onerror=fail):
        folders[:] = sorted(
            name for name in folders
            if not name.startswith(".") and not (Path(directory) / name).is_symlink()
        )
        for name in sorted(names):
            path = Path(directory) / name
            if path.is_symlink() or path.suffix.lower() not in EXTENSIONS:
                continue
            info = path.stat()
            files.append({
                "relative_path": path.relative_to(library).as_posix(),
                "bytes": info.st_size,
                "status": "zero-byte" if info.st_size == 0 else "nonempty-unverified",
            })
    payload = {
        "root": str(library),
        "scanned_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "method": "directory metadata only; no content or edition verification",
        "files": sorted(files, key=lambda item: item["relative_path"].casefold()),
    }
    catalog.parent.mkdir(parents=True, exist_ok=True)
    temporary = catalog.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(catalog)
    empty = sum(item["bytes"] == 0 for item in files)
    print(f"Cataloged {len(files)} files ({empty} zero-byte); external files unchanged.")


def search(catalog: Path, words: list[str]) -> None:
    payload = json.loads(catalog.read_text(encoding="utf-8"))
    matches = [
        item for item in payload["files"]
        if all(word.casefold() in item["relative_path"].casefold() for word in words)
    ]
    for item in matches:
        print(f"{item['status']} | {item['bytes']} bytes | {Path(payload['root']) / item['relative_path']}")
    if not matches:
        print("No matching catalog entries.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("scan", help="refresh the repository catalog from file metadata")
    query = commands.add_parser("search", help="search the saved filename catalog")
    query.add_argument("words", nargs="+")
    args = parser.parse_args()
    try:
        library, catalog = configuration()
        if args.command == "scan":
            scan(library, catalog)
        else:
            search(catalog, args.words)
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
