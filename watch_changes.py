#!/usr/bin/env python3
"""Periodically report file changes under a project directory."""

from __future__ import annotations

import argparse
import hashlib
import os
import time
from datetime import datetime
from pathlib import Path


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def snapshot(root: Path) -> dict[Path, str]:
    result: dict[Path, str] = {}
    for current, directories, filenames in os.walk(root):
        directories[:] = [name for name in directories if name != ".git"]
        current_path = Path(current)
        for filename in filenames:
            path = current_path / filename
            try:
                result[path.relative_to(root)] = file_digest(path)
            except OSError as error:
                print(f"Nelze přečíst {path.relative_to(root)}: {error}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pravidelně kontroluje přidané, změněné a smazané soubory."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Kořenová složka projektu (výchozí: složka tohoto skriptu).",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=60,
        metavar="SEKUND",
        help="Interval kontroly v sekundách (výchozí: 60).",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    if args.interval <= 0:
        parser.error("--interval musí být větší než nula")
    if not root.is_dir():
        parser.error(f"Složka neexistuje: {root}")

    previous = snapshot(root)
    print(f"Sleduji {root} každých {args.interval:g} s. Ukončení: Ctrl+C")

    try:
        while True:
            time.sleep(args.interval)
            current = snapshot(root)
            added = sorted(current.keys() - previous.keys(), key=str)
            deleted = sorted(previous.keys() - current.keys(), key=str)
            changed = sorted(
                (path for path in current.keys() & previous.keys()
                 if current[path] != previous[path]),
                key=str,
            )

            if added or changed or deleted:
                print(f"\n[{datetime.now().astimezone().isoformat(timespec='seconds')}]")
                for label, paths in (
                    ("Přidáno", added),
                    ("Změněno", changed),
                    ("Smazáno", deleted),
                ):
                    for path in paths:
                        print(f"{label}: {path}")

            previous = current
    except KeyboardInterrupt:
        print("\nKontrola ukončena.")


if __name__ == "__main__":
    main()
