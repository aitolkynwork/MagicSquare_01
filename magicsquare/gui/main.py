"""Qt application entry (import PyQt only from this package subtree)."""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from magicsquare.gui.window import MainWindow


def run_app() -> int:
    """Start the Magic Square screen; return process exit code."""
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    return app.exec()
