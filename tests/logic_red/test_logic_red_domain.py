"""Domain / logic RED skeletons — dual-track TDD. Replace fail() with real asserts when implementing."""

import pytest


def test_find_blank_coords_returns_two_pairs_row_major_one_indexed():
    pytest.fail("RED: LOGIC-RED-01 — find_blank_coords: two blanks, row-major, 1-based (D7).")


def test_find_not_exist_nums_returns_two_missing_sorted_ascending():
    pytest.fail("RED: LOGIC-RED-02 — find_not_exist_nums: two missing, ascending (D4).")


def test_is_magic_square_true_when_all_sums_equal_thirty_four():
    pytest.fail("RED: LOGIC-RED-03a — is_magic_square True on valid order-4 magic (D5).")


def test_is_magic_square_false_when_any_row_sum_not_thirty_four():
    pytest.fail("RED: LOGIC-RED-03b — is_magic_square False when a row ≠ 34 (D5).")


def test_is_magic_square_false_when_any_column_sum_not_thirty_four():
    pytest.fail("RED: LOGIC-RED-03c — is_magic_square False when a column ≠ 34 (D5).")


def test_is_magic_square_false_when_main_diagonal_sum_not_thirty_four():
    pytest.fail("RED: LOGIC-RED-03d — is_magic_square False when main diagonal ≠ 34 (D5).")


def test_is_magic_square_false_when_anti_diagonal_sum_not_thirty_four():
    pytest.fail("RED: LOGIC-RED-03e — is_magic_square False when anti-diagonal ≠ 34 (D5).")


def test_solution_prefers_smaller_missing_at_first_blank_when_that_completion_is_magic():
    pytest.fail("RED: LOGIC-RED-04a — solution: smaller→first blank when valid (D6).")


def test_solution_swaps_numbers_when_only_reverse_assignment_is_magic():
    pytest.fail("RED: LOGIC-RED-04b — solution: reverse (n1,n2) when only swap works (D6).")


def test_solution_output_length_six_and_coords_one_indexed():
    pytest.fail("RED: LOGIC-RED-04c — solution: len 6, 1-based coords (D7, output schema).")
