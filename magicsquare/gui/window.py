"""Main window: 4×4 grid, Solve → boundary ``solve_ui_matrix``."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from magicsquare.boundary import UiBoundaryError, solve_ui_matrix
from magicsquare.constants import MATRIX_SIZE


def _default_demo_matrix() -> list[list[int]]:
    """Classical order-4 magic with two corners blank — solvable via reverse placement."""
    return [
        [0, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 0],
    ]


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Magic Square 4×4 — MVP")
        self._cells: list[list[QSpinBox]] = []
        root = QVBoxLayout(self)

        grid_box = QGroupBox("Grid (0 = blank)")
        grid_layout = QGridLayout(grid_box)
        demo = _default_demo_matrix()
        for r in range(MATRIX_SIZE):
            row_widgets: list[QSpinBox] = []
            for c in range(MATRIX_SIZE):
                sp = QSpinBox()
                sp.setRange(0, 16)
                sp.setSpecialValueText("0")
                sp.setValue(demo[r][c])
                sp.setAlignment(Qt.AlignmentFlag.AlignCenter)
                grid_layout.addWidget(sp, r, c)
                row_widgets.append(sp)
            self._cells.append(row_widgets)
        root.addWidget(grid_box)

        btn_row = QHBoxLayout()
        solve_btn = QPushButton("Solve")
        solve_btn.clicked.connect(self._on_solve)
        btn_row.addWidget(solve_btn)
        btn_row.addStretch()
        root.addLayout(btn_row)

        out_box = QGroupBox("Result (r1, c1, n1, r2, c2, n2)")
        out_layout = QVBoxLayout(out_box)
        self._result = QLabel("—")
        self._result.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        out_layout.addWidget(self._result)
        root.addWidget(out_box)

    def _read_matrix(self) -> list[list[int]]:
        return [
            [self._cells[r][c].value() for c in range(MATRIX_SIZE)]
            for r in range(MATRIX_SIZE)
        ]

    def _on_solve(self) -> None:
        matrix = self._read_matrix()
        try:
            out = solve_ui_matrix(matrix)
            self._result.setText(", ".join(str(x) for x in out))
        except UiBoundaryError as err:
            self._result.setText("—")
            QMessageBox.warning(self, "Cannot solve", err.message)
