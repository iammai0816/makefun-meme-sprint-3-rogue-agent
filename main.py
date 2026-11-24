"""Meme Sprint 3: AI Agent Goes Rogue — entry program.

Copies the meme image (entry.png, made by the agent in the build
session) to $MAKEFUN_OUTPUT_DIR/entry.png for the judge.

Deterministic: the same input bytes produce the same output bytes on
every run. Standard library only; no network access.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _png_dimensions(path: str) -> tuple:
    """Return (width, height) of a PNG, raising ValueError if it is not one."""
    with open(path, "rb") as fh:
        header = fh.read(33)
    if len(header) < 33 or not header.startswith(PNG_SIGNATURE):
        raise ValueError(f"{path} is not a PNG image")
    if header[12:16] != b"IHDR":
        raise ValueError(f"{path} has no IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    if not os.path.isfile(SRC):
        print(f"missing source image: {SRC}", file=sys.stderr)
        return 1
    width, height = _png_dimensions(SRC)
    if width > 1024 or height > 1024:
        print(f"meme too large: {width}x{height} (max 1024x1024)", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    os.chmod(dst, 0o644)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
