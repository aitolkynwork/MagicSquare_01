"""Launch the screen: ``python -m magicsquare`` (same app as ``magicsquare.gui``)."""

from __future__ import annotations

import sys

from magicsquare.gui.main import run_app

if __name__ == "__main__":
    sys.exit(run_app())
