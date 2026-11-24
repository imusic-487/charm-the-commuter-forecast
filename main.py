"""Charm the Commuter: Forecast a City That Isn't.

Reads the one-line forecast from line.txt and writes it to
/output/entry.txt, byte for byte.

The gate allows UTF-8 text of 1 to 140 characters that is not only
white space, so the program checks exactly that before writing and
also insists the entry is one line, then refuses to write anything
that fails. It then reads the file back
and compares it with the source, so a short write or a stray
transformation is caught here instead of on the server.

Set MAKEFUN_OUTPUT_DIR to write somewhere else when testing
locally. Standard library only; no network, no randomness, no
clock reads, so every run writes the same bytes.
"""

import os
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "line.txt"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_FILE = OUT_DIR / "entry.txt"

MAX_CHARS = 140


def load_line() -> tuple[bytes, str]:
    raw = SOURCE.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"line.txt is not valid UTF-8: {exc}") from exc
    return raw, text


def check_line(text: str) -> None:
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} characters, allowed 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def write_entry(raw: bytes) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_bytes(raw)
    back = OUT_FILE.read_bytes()
    if back != raw:
        raise SystemExit(
            f"wrote {len(back)} bytes but line.txt has {len(raw)}; "
            "the copy does not match the source"
        )


def main() -> None:
    raw, text = load_line()
    check_line(text)
    write_entry(raw)
    print(
        f"wrote {OUT_FILE}: {len(text)} characters, "
        f"{len(raw)} bytes, one line"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        if exc.code:
            print(f"ERROR: {exc.code}", file=sys.stderr)
            sys.exit(1)
        raise
