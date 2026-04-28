package com.magicsquare.red;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

/** UI / boundary RED skeletons — dual-track TDD. */
class UiRedBoundaryTest {

    @Test
    void test_ui_rejects_non_4x4_matrix_raises_or_structured_error() {
        fail("RED: UI-RED-01 — non-4×4 input must fail before domain (D1 / E_WRONG_SIZE).");
    }

    @Test
    void test_ui_rejects_blank_count_not_two_raises_or_structured_error() {
        fail("RED: UI-RED-02 — exactly two blanks required (D2 / E_BLANK_COUNT).");
    }

    @Test
    void test_ui_rejects_value_outside_zero_to_sixteen_raises_or_structured_error() {
        fail("RED: UI-RED-03 — cell values must be 0 or 1–16 (D2 / E_VALUE_RANGE).");
    }

    @Test
    void test_ui_rejects_duplicate_nonzero_raises_or_structured_error() {
        fail("RED: UI-RED-04 — no duplicate non-zero values (D3 / E_DUPLICATE_VALUE).");
    }

    @Test
    void test_ui_success_returns_array_of_length_six() {
        fail("RED: UI-RED-05 — success output int[6] (output schema).");
    }

    @Test
    void test_ui_success_coordinates_are_one_indexed() {
        fail("RED: UI-RED-06 — 1-based coords in blank row-major order (D7).");
    }
}
