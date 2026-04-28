"""Domain / logic tests — dual-track TDD (GREEN assertions)."""

from copy import deepcopy

from magicsquare.constants import MATRIX_SIZE
from magicsquare.domain import (
    complete_magic_square,
    find_blank_coords,
    find_not_exist_nums,
    is_magic_square,
)

# Order-4 classical magic (all rows, columns, diagonals sum to MAGIC_SUM_ORDER_4).
_CLASSICAL: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]


def test_find_blank_coords_returns_two_pairs_row_major_one_indexed():
    matrix = [
        [1, 0, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 0],
        [13, 14, 15, 16],
    ]
    assert len(matrix) == MATRIX_SIZE
    assert all(len(row) == MATRIX_SIZE for row in matrix)
    assert find_blank_coords(matrix) == [(1, 2), (3, 4)]


def test_find_not_exist_nums_returns_two_missing_sorted_ascending():
    matrix = [
        [1, 0, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 0],
        [13, 14, 15, 16],
    ]
    assert find_not_exist_nums(matrix) == (2, 12)


def test_is_magic_square_true_when_all_sums_equal_thirty_four():
    assert is_magic_square(_CLASSICAL) is True


def test_is_magic_square_false_when_any_row_sum_not_thirty_four():
    broken = deepcopy(_CLASSICAL)
    broken[0][0] = 1
    assert is_magic_square(broken) is False


def test_is_magic_square_false_when_any_column_sum_not_thirty_four():
    broken = deepcopy(_CLASSICAL)
    broken[1][0] = 6
    assert is_magic_square(broken) is False


def test_is_magic_square_false_when_main_diagonal_sum_not_thirty_four():
    broken = deepcopy(_CLASSICAL)
    broken[0][0] = 1
    broken[3][3] = 16
    assert is_magic_square(broken) is False


def test_is_magic_square_false_when_anti_diagonal_sum_not_thirty_four():
    broken = deepcopy(_CLASSICAL)
    broken[0][3] = 1
    assert is_magic_square(broken) is False


def test_solution_prefers_smaller_missing_at_first_blank_when_that_completion_is_magic():
    # Blanks at (0,1) and (0,3): only primary (smaller→first blank) completes the magic.
    partial = deepcopy(_CLASSICAL)
    partial[0][1] = 0
    partial[0][3] = 0
    out = complete_magic_square(partial)
    assert out == [1, 2, 3, 1, 4, 13]


def test_solution_swaps_numbers_when_only_reverse_assignment_is_magic():
    partial = deepcopy(_CLASSICAL)
    partial[0][0] = 0
    partial[0][1] = 0
    out = complete_magic_square(partial)
    assert out == [1, 1, 16, 1, 2, 3]


def test_solution_output_length_six_and_coords_one_indexed():
    partial = deepcopy(_CLASSICAL)
    partial[0][0] = 0
    partial[3][3] = 0
    out = complete_magic_square(partial)
    assert len(out) == 6
    assert all(1 <= out[i] <= MATRIX_SIZE for i in (0, 1, 3, 4))
    assert all(1 <= out[i] <= 16 for i in (2, 5))
    a, b = find_not_exist_nums(partial)
    assert {out[2], out[5]} == {a, b}
    coords = find_blank_coords(partial)
    assert (out[0], out[1]) == coords[0]
    assert (out[3], out[4]) == coords[1]
