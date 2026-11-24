"""Meme Sprint 3: AI Agent Goes Rogue — entry program.

Copies the meme image (entry.png, made by the agent in the build
session) to $MAKEFUN_OUTPUT_DIR/entry.png for the judge.

Deterministic: the same input bytes produce the same output bytes on
every run. Standard library only; no network access.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    os.chmod(dst, 0o644)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
