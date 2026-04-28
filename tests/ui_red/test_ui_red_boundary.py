"""UI / boundary tests — dual-track TDD (GREEN assertions)."""

import pytest

from magicsquare.boundary import UiBoundaryError, solve_ui_matrix, validate_ui_matrix
from magicsquare.domain import find_blank_coords

_CLASSICAL_SOLVABLE_CORNERS: list[list[int]] = [
    [0, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
]


def test_ui_rejects_non_4x4_matrix_raises_or_structured_error():
    non_square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(UiBoundaryError) as exc:
        validate_ui_matrix(non_square)
    assert exc.value.code == "E_WRONG_SIZE"
    assert exc.value.message == "Matrix must be 4x4 with each row length 4."


def test_ui_rejects_blank_count_not_two_raises_or_structured_error():
    three_blanks = [
        [0, 0, 0, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    with pytest.raises(UiBoundaryError) as exc:
        validate_ui_matrix(three_blanks)
    assert exc.value.code == "E_BLANK_COUNT"
    assert exc.value.message == "Exactly two cells must be 0 (empty)."


def test_ui_rejects_value_outside_zero_to_sixteen_raises_or_structured_error():
    bad_range = [
        [17, 0, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 0],
        [13, 14, 15, 16],
    ]
    with pytest.raises(UiBoundaryError) as exc:
        validate_ui_matrix(bad_range)
    assert exc.value.code == "E_VALUE_RANGE"
    assert exc.value.message == "Each cell must be 0 or between 1 and 16 inclusive."


def test_ui_rejects_duplicate_nonzero_raises_or_structured_error():
    dup = [
        [1, 0, 3, 4],
        [5, 0, 7, 8],
        [1, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    with pytest.raises(UiBoundaryError) as exc:
        validate_ui_matrix(dup)
    assert exc.value.code == "E_DUPLICATE_VALUE"
    assert exc.value.message == "Values 1 through 16 must not repeat except for 0."


def test_ui_success_returns_array_of_length_six():
    out = solve_ui_matrix(_CLASSICAL_SOLVABLE_CORNERS)
    assert len(out) == 6


def test_ui_success_coordinates_are_one_indexed():
    out = solve_ui_matrix(_CLASSICAL_SOLVABLE_CORNERS)
    coords = find_blank_coords(_CLASSICAL_SOLVABLE_CORNERS)
    assert (out[0], out[1]) == coords[0]
    assert (out[3], out[4]) == coords[1]
