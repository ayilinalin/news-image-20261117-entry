#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117.

Copies the pre-rendered front-page image (entry.png, in this repository)
to $MAKEFUN_OUTPUT_DIR/entry.png.

The image is a newspaper front page summing up the world news of
Tuesday 17 November 2026: the date banner, the Crimea/Kyiv bridge
strikes, the third US carrier joining the fleet as a tanker burns near
Hormuz, the Xi-Trump-Putin summit set for Thursday, and the five EU
states planning a Rwanda return hub.

Standard library only. No network. Deterministic: a byte-for-byte copy,
so every run writes identical output.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1_048_576  # 1 MiB, the competition limit
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 1


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return _fail("MAKEFUN_OUTPUT_DIR is not set")

    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        return _fail(f"source image not found: {source}")

    size = source.stat().st_size
    if size > MAX_BYTES:
        return _fail(f"source image is {size} bytes, over the 1 MiB limit")

    with source.open("rb") as handle:
        if handle.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
            return _fail("source image is not a PNG file")

    destination = Path(out_dir) / OUTPUT_NAME
    destination.parent.mkdir(parents=True, exist_ok=True)

    shutil.copyfile(source, destination)
    os.chmod(destination, 0o644)

    # Verify the copy is byte-identical to the source.
    src_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    dst_hash = hashlib.sha256(destination.read_bytes()).hexdigest()
    if src_hash != dst_hash:
        return _fail("copied image differs from source")

    print(f"wrote {destination} ({size} bytes, sha256 {dst_hash[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
