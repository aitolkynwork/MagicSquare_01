"""UI / boundary RED skeletons — dual-track TDD. Replace fail() with real asserts when implementing."""

import pytest


def test_ui_rejects_non_4x4_matrix_raises_or_structured_error():
    pytest.fail("RED: UI-RED-01 — non-4×4 input must fail before domain (D1 / E_WRONG_SIZE).")


def test_ui_rejects_blank_count_not_two_raises_or_structured_error():
    pytest.fail("RED: UI-RED-02 — exactly two blanks required (D2 / E_BLANK_COUNT).")


def test_ui_rejects_value_outside_zero_to_sixteen_raises_or_structured_error():
    pytest.fail("RED: UI-RED-03 — cell values must be 0 or 1–16 (D2 / E_VALUE_RANGE).")


def test_ui_rejects_duplicate_nonzero_raises_or_structured_error():
    pytest.fail("RED: UI-RED-04 — no duplicate non-zero values (D3 / E_DUPLICATE_VALUE).")


def test_ui_success_returns_array_of_length_six():
    pytest.fail("RED: UI-RED-05 — success output int[6] (output schema).")


def test_ui_success_coordinates_are_one_indexed():
    pytest.fail("RED: UI-RED-06 — 1-based coords in blank row-major order (D7).")
