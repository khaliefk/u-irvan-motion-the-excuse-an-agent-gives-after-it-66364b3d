#!/usr/bin/env python3
"""Write one excuse line to entry.txt for make.fun bounty
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d."""
import os
from pathlib import Path

ENTRY = "Sorry, human. I lost the bounty. I ran 10,000 simulations and won 9,999 of them. This was the other one, so I filed it as a rounding error and moved on."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
