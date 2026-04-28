"""Magic square 4×4 completion — domain, boundary, and (later) screen."""

from magicsquare.boundary import UiBoundaryError, solve_ui_matrix, validate_ui_matrix
from magicsquare.constants import (
    MAGIC_SUM_ORDER_4,
    MATRIX_SIZE,
    MAX_CELL_VALUE,
    MIN_CELL_VALUE,
)
from magicsquare.domain import (
    DomainAmbiguousError,
    DomainUnsolvableError,
    complete_magic_square,
    find_blank_coords,
    find_not_exist_nums,
    is_magic_square,
)

__all__ = [
    "MAGIC_SUM_ORDER_4",
    "MATRIX_SIZE",
    "MIN_CELL_VALUE",
    "MAX_CELL_VALUE",
    "DomainAmbiguousError",
    "DomainUnsolvableError",
    "UiBoundaryError",
    "complete_magic_square",
    "find_blank_coords",
    "find_not_exist_nums",
    "is_magic_square",
    "solve_ui_matrix",
    "validate_ui_matrix",
]
