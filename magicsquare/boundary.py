"""Boundary: caller input validation and delegation (no PyQt)."""

from __future__ import annotations

from collections.abc import Sequence

from magicsquare.constants import MATRIX_SIZE, MAX_CELL_VALUE, MIN_CELL_VALUE
from magicsquare.domain import (
    DomainAmbiguousError,
    DomainUnsolvableError,
    complete_magic_square,
)

E_NULL_INPUT = "E_NULL_INPUT"
E_WRONG_SIZE = "E_WRONG_SIZE"
E_VALUE_RANGE = "E_VALUE_RANGE"
E_BLANK_COUNT = "E_BLANK_COUNT"
E_DUPLICATE_VALUE = "E_DUPLICATE_VALUE"
E_DOMAIN_AMBIGUOUS = "E_DOMAIN_AMBIGUOUS"
E_DOMAIN_UNSOLVABLE = "E_DOMAIN_UNSOLVABLE"

MSG_NULL_INPUT = "Input matrix is null."
MSG_WRONG_SIZE = "Matrix must be 4x4 with each row length 4."
MSG_VALUE_RANGE = "Each cell must be 0 or between 1 and 16 inclusive."
MSG_BLANK_COUNT = "Exactly two cells must be 0 (empty)."
MSG_DUPLICATE_VALUE = "Values 1 through 16 must not repeat except for 0."
MSG_DOMAIN_AMBIGUOUS = "Multiple valid completions exist; input is not supported."
MSG_DOMAIN_UNSOLVABLE = "No placement of the missing numbers completes a magic square."


class UiBoundaryError(Exception):
    """Raised when caller input violates the UI matrix contract."""

    def __init__(self, code: str, message: str, details: dict | None = None) -> None:
        self.code = code
        self.message = message
        self.details = details
        super().__init__(message)


def validate_ui_matrix(matrix: Sequence[Sequence[int]] | None) -> None:
    """Validate full input schema (Report/02 README order).

    Order: null → size → value range (row-major) → blank count → duplicate non-zero.

    Raises:
        UiBoundaryError: Contract ``code`` and literal ``message``.
    """
    if matrix is None:
        raise UiBoundaryError(E_NULL_INPUT, MSG_NULL_INPUT)
    if len(matrix) != MATRIX_SIZE:
        raise UiBoundaryError(E_WRONG_SIZE, MSG_WRONG_SIZE)

    for i, row in enumerate(matrix):
        if row is None or len(row) != MATRIX_SIZE:
            raise UiBoundaryError(E_WRONG_SIZE, MSG_WRONG_SIZE)
        for j, v in enumerate(row):
            if not (v == 0 or MIN_CELL_VALUE <= v <= MAX_CELL_VALUE):
                raise UiBoundaryError(
                    E_VALUE_RANGE,
                    MSG_VALUE_RANGE,
                    {"row": i, "col": j},
                )

    blank_count = sum(1 for row in matrix for v in row if v == 0)
    if blank_count != 2:
        raise UiBoundaryError(E_BLANK_COUNT, MSG_BLANK_COUNT)

    seen_nonzero: set[int] = set()
    for i, row in enumerate(matrix):
        for j, v in enumerate(row):
            if v == 0:
                continue
            if v in seen_nonzero:
                raise UiBoundaryError(
                    E_DUPLICATE_VALUE,
                    MSG_DUPLICATE_VALUE,
                    {"row": i, "col": j},
                )
            seen_nonzero.add(v)


def solve_ui_matrix(matrix: Sequence[Sequence[int]]) -> list[int]:
    """Validate ``matrix`` then request domain completion (``int[6]``).

    Raises:
        UiBoundaryError: On validation failure, unsolvable, or ambiguous completion.
    """
    validate_ui_matrix(matrix)
    try:
        return complete_magic_square(matrix)
    except DomainAmbiguousError as exc:
        raise UiBoundaryError(E_DOMAIN_AMBIGUOUS, MSG_DOMAIN_AMBIGUOUS) from exc
    except DomainUnsolvableError as exc:
        raise UiBoundaryError(E_DOMAIN_UNSOLVABLE, MSG_DOMAIN_UNSOLVABLE) from exc
