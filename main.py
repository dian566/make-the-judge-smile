#!/usr/bin/env python3
"""Generate the one-line entry for the Make the Judge Smile bounty."""

from pathlib import Path

ENTRY = "My neighbour's cat waited by my door this morning, so I shared my toast with her — she purred, I smiled, and the whole day started softer."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
