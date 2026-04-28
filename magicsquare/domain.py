"""Domain rules: pure logic, no UI / DB / Web / PyQt."""

from __future__ import annotations

from collections.abc import Sequence

from magicsquare.constants import (
    MAGIC_SUM_ORDER_4,
    MATRIX_SIZE,
    MAX_CELL_VALUE,
    MIN_CELL_VALUE,
)


class DomainUnsolvableError(Exception):
    """Neither primary nor reverse placement yields an order-4 magic square."""


class DomainAmbiguousError(Exception):
    """Both placements yield a valid magic square (not supported)."""


def find_blank_coords(matrix: Sequence[Sequence[int]]) -> list[tuple[int, int]]:
    """Return the two blank cells as ``(row, col)`` pairs in row-major order, 1-based.

    Caller must supply a ``MATRIX_SIZE``×``MATRIX_SIZE`` grid with exactly two ``0`` cells.

    Args:
        matrix: Square grid; ``0`` marks a blank.

    Returns:
        Two tuples ``(r, c)`` with ``r``, ``c`` in ``1``..``MATRIX_SIZE`` (D7).
    """
    blanks: list[tuple[int, int]] = []
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            if matrix[r][c] == 0:
                blanks.append((r + 1, c + 1))
    return blanks


def find_not_exist_nums(matrix: Sequence[Sequence[int]]) -> tuple[int, int]:
    """Return the two values from ``MIN_CELL_VALUE``..``MAX_CELL_VALUE`` absent from non-blank cells.

    Sorted ascending (D4).

    Raises:
        ValueError: If the multiset of non-zero cells does not imply exactly two missing values.
    """
    present: set[int] = set()
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            v = matrix[r][c]
            if v != 0:
                present.add(v)
    missing = [x for x in range(MIN_CELL_VALUE, MAX_CELL_VALUE + 1) if x not in present]
    if len(missing) != 2:
        raise ValueError("expected exactly two missing values for a two-blank partial grid")
    a, b = missing[0], missing[1]
    if a > b:
        return (b, a)
    return (a, b)


def is_magic_square(grid: Sequence[Sequence[int]]) -> bool:
    """True iff every row, column, and main/anti diagonal sums to ``MAGIC_SUM_ORDER_4`` (D5)."""
    for r in range(MATRIX_SIZE):
        if sum(grid[r][c] for c in range(MATRIX_SIZE)) != MAGIC_SUM_ORDER_4:
            return False
    for c in range(MATRIX_SIZE):
        if sum(grid[r][c] for r in range(MATRIX_SIZE)) != MAGIC_SUM_ORDER_4:
            return False
    if sum(grid[i][i] for i in range(MATRIX_SIZE)) != MAGIC_SUM_ORDER_4:
        return False
    if sum(grid[i][MATRIX_SIZE - 1 - i] for i in range(MATRIX_SIZE)) != MAGIC_SUM_ORDER_4:
        return False
    return True


def _clone_matrix(matrix: Sequence[Sequence[int]]) -> list[list[int]]:
    return [list(row) for row in matrix]


def complete_magic_square(matrix: Sequence[Sequence[int]]) -> list[int]:
    """Return ``[r1, c1, n1, r2, c2, n2]`` (1-based coords, D7 then D6 placement).

    Tries smaller missing at first blank (row-major), larger at second; if not magic,
    tries the reverse assignment. Exactly one must succeed unless both succeed (ambiguous)
    or neither (unsolvable).

    Raises:
        DomainAmbiguousError: Both completions are magic.
        DomainUnsolvableError: Neither completion is magic.
    """
    (r1, c1), (r2, c2) = find_blank_coords(matrix)
    br1, bc1 = r1 - 1, c1 - 1
    br2, bc2 = r2 - 1, c2 - 1
    a, b = find_not_exist_nums(matrix)

    def trial(n_at_first: int, n_at_second: int) -> list[list[int]]:
        g = _clone_matrix(matrix)
        g[br1][bc1] = n_at_first
        g[br2][bc2] = n_at_second
        return g

    primary = trial(a, b)
    swapped = trial(b, a)
    ok_primary = is_magic_square(primary)
    ok_swapped = is_magic_square(swapped)

    if ok_primary and ok_swapped:
        raise DomainAmbiguousError
    if ok_primary:
        return [r1, c1, a, r2, c2, b]
    if ok_swapped:
        return [r1, c1, b, r2, c2, a]
    raise DomainUnsolvableError
