# Test case specification (English)

Document layout matches the requested vertical fields. **Per test case:** repeat the block from **Test ID** through **Special procedures**. Header rows apply to the whole document (fill project metadata as needed).

---

## Document header (once)

| Field | Value |
|--------|--------|
| **Test case (document)** | Magic Square 4×4 — manual / automated test case set |
| **Project name** | MagicSquare_01 (4×4 magic square completion) |
| **Target system** | Functions under test: `find_blank_coords`, `is_magic_square`, `solution` (or project equivalents per Report/02 naming) |

| Field | Value | Field | Value | Field | Value | Field | Value |
|--------|--------|--------|--------|--------|--------|--------|--------|
| **Phase** | *(e.g. System test)* | **Author** | | **Approver** | | **Document status** | Draft |
| **Created date** | | **Version** | 1.0 | **Test scope** | Unit / integration for 4×4 magic helpers | **Test organization** | |

---

## TC-MS-A-001

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-A-001 |
| **Test date** | |
| **Test purpose** | Verify that coordinates of cells with value `0` (blanks) are detected correctly in a 4×4 matrix when there are exactly two blanks. |
| **Function under test** | `find_blank_coords` (or equivalent: ordered blank detection) |
| **Input / prerequisites** | 4×4 matrix with zeros at positions equivalent to (row 1, col 3) and (row 3, col 3) per the original matrix layout used in the spec (see matrix in source table). |
| **Test steps** | 1. **Given** the input matrix with two blanks at the specified positions.<br>2. **When** `find_blank_coords` is invoked with that matrix.<br>3. **Then** the returned list of coordinates matches the expected blank positions in the required ordering (e.g. row-major). |
| **Test environment** | Python 3.10+; pytest; local or CI. |
| **Prerequisites** | Matrix is 4×4; exactly two cells are `0`; remaining values valid for the scenario. |
| **Pass / fail criteria** | Return value equals `[(1,3), (3,3)]` if the spec uses 1-based indexing as in the source table; otherwise align coordinates with project contract (D7 row-major, 1-based). **Pass:** exact match to expected list. **Fail:** any mismatch or exception not specified as allowed. |
| **Special procedures** | None. |
| **Priority** | P1 |

---

## TC-MS-A-002

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-A-002 |
| **Test date** | |
| **Test purpose** | Verify blank detection when blanks include “first” and “last” positions in the grid (corner coverage). |
| **Function under test** | `find_blank_coords` |
| **Input / prerequisites** | 4×4 matrix with blanks at top-left and bottom-right (e.g. positions corresponding to `(0,0)` and `(3,3)` in 0-based source notation). |
| **Test steps** | 1. **Given** the matrix with blanks at first and last cells.<br>2. **When** `find_blank_coords` is called.<br>3. **Then** returned coordinates are `[(0,0), (3,3)]` in the same indexing convention as the source spec, or the project-mapped equivalent. |
| **Test environment** | Same as TC-MS-A-001. |
| **Prerequisites** | Valid matrix shape; blanks only where defined for this case. |
| **Pass / fail criteria** | Returned list matches expected pair in correct order. **Fail:** wrong order, missing coordinate, or extra entries. |
| **Special procedures** | Confirm project rule: 0-based vs 1-based coordinates and row-major order (D7). |
| **Priority** | P1 |

---

## TC-MS-A-003

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-A-003 |
| **Test date** | |
| **Test purpose** | Verify behavior when there are **no** blanks (no `0` cells): function should report no blank coordinates. |
| **Function under test** | `find_blank_coords` |
| **Input / prerequisites** | Fully filled 4×4 matrix (no zeros). |
| **Test steps** | 1. **Given** a 4×4 matrix with no `0` values.<br>2. **When** `find_blank_coords` is called.<br>3. **Then** an empty list is returned. |
| **Test environment** | Same as TC-MS-A-001. |
| **Prerequisites** | No cell equals `0`. |
| **Pass / fail criteria** | Return value is `[]`. **Fail:** non-empty list or unhandled error if API defines no-error for this case. |
| **Special procedures** | **Remark (source):** boundary — zero blank count. |
| **Priority** | P2 |

---

## TC-MS-A-004

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-A-004 |
| **Test date** | |
| **Test purpose** | Verify detection when exactly **one** blank exists. |
| **Function under test** | `find_blank_coords` |
| **Input / prerequisites** | 4×4 matrix with a single `0` (e.g. at position corresponding to `(3,2)` in source table). |
| **Test steps** | 1. **Given** one blank cell.<br>2. **When** `find_blank_coords` is called.<br>3. **Then** a singleton list with that coordinate is returned. |
| **Test environment** | Same as TC-MS-A-001. |
| **Prerequisites** | Exactly one `0`. |
| **Pass / fail criteria** | Return equals `[(3,2)]` per source indexing, or project-equivalent. **Fail:** wrong cell or wrong list length. |
| **Special procedures** | Note: MagicSquare_01 completion contract expects **exactly two** blanks; this TC may apply only to a generic helper or a relaxed API — align with product decision. |
| **Priority** | P2 |

---

## TC-MS-A-005

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-A-005 |
| **Test date** | |
| **Test purpose** | Verify listing when **three or more** blanks exist. |
| **Function under test** | `find_blank_coords` |
| **Input / prerequisites** | 4×4 matrix with three (or more) `0` cells (e.g. `(0,0), (1,1), (3,3)` in source notation). |
| **Test steps** | 1. **Given** multiple blanks.<br>2. **When** `find_blank_coords` is called.<br>3. **Then** all blank coordinates are returned in the specified order. |
| **Test environment** | Same as TC-MS-A-001. |
| **Prerequisites** | Three or more zeros in grid. |
| **Pass / fail criteria** | Return equals `[(0,0), (1,1), (3,3)]` per source, or full ordered list per contract. **Fail:** omission, wrong order, or wrong length. |
| **Special procedures** | None. |
| **Priority** | P3 |

---

## TC-MS-B-001

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-B-001 |
| **Test date** | |
| **Test purpose** | Verify that a **completed** valid 4×4 magic square is recognized: all row, column, and main diagonal sums equal the magic constant (34 for order 4). |
| **Function under test** | `is_magic_square` |
| **Input / prerequisites** | A valid completed 4×4 magic square (all cells 1–16, magic property satisfied). |
| **Test steps** | 1. **Given** a completed magic square matrix.<br>2. **When** `is_magic_square` is called.<br>3. **Then** the function returns `True`. |
| **Test environment** | Same as Group A. |
| **Prerequisites** | All rows, columns, both main diagonals sum to 34; values consistent with a magic square. |
| **Pass / fail criteria** | Return is `True`. **Fail:** `False` or exception. |
| **Special procedures** | **Remark:** magic sum = 34 (order 4). |
| **Priority** | P1 |

---

## TC-MS-B-002

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-B-002 |
| **Test date** | |
| **Test purpose** | Verify `False` when **at least one row** does not sum to the magic constant. |
| **Function under test** | `is_magic_square` |
| **Input / prerequisites** | 4×4 matrix that fails row-sum equality (intentionally broken row). |
| **Test steps** | 1. **Given** a matrix with a row sum mismatch.<br>2. **When** `is_magic_square` is called.<br>3. **Then** return `False`. |
| **Test environment** | Same as Group A. |
| **Prerequisites** | All other dimensions filled so only row condition fails magic check. |
| **Pass / fail criteria** | Returns `False`. **Fail:** `True`. |
| **Special procedures** | None. |
| **Priority** | P1 |

---

## TC-MS-B-003

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-B-003 |
| **Test date** | |
| **Test purpose** | Verify `False` when **at least one column** does not sum to the magic constant. |
| **Function under test** | `is_magic_square` |
| **Input / prerequisites** | 4×4 matrix with a column sum mismatch. |
| **Test steps** | 1. **Given** column sum error.<br>2. **When** `is_magic_square` is called.<br>3. **Then** return `False`. |
| **Test environment** | Same as Group A. |
| **Prerequisites** | Column defect only (rows and diagonals may still sum to 34 individually if constructed that way — use a matrix where column fails). |
| **Pass / fail criteria** | Returns `False`. |
| **Special procedures** | None. |
| **Priority** | P1 |

---

## TC-MS-B-004

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-B-004 |
| **Test date** | |
| **Test purpose** | Verify `False` when the **main diagonal** sum is not the magic constant. |
| **Function under test** | `is_magic_square` |
| **Input / prerequisites** | 4×4 matrix with main-diagonal sum ≠ 34. |
| **Test steps** | 1. **Given** main diagonal incorrect.<br>2. **When** `is_magic_square` is called.<br>3. **Then** return `False`. |
| **Test environment** | Same as Group A. |
| **Prerequisites** | Rows/columns may pass or fail per construction; diagonal must fail per TC intent. |
| **Pass / fail criteria** | Returns `False`. |
| **Special procedures** | None. |
| **Priority** | P1 |

---

## TC-MS-B-005

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-B-005 |
| **Test date** | |
| **Test purpose** | Verify `False` when the **anti-diagonal** (secondary diagonal) sum is not the magic constant. |
| **Function under test** | `is_magic_square` |
| **Input / prerequisites** | 4×4 matrix where anti-diagonal sum ≠ 34. |
| **Test steps** | 1. **Given** anti-diagonal defect.<br>2. **When** `is_magic_square` is called.<br>3. **Then** return `False`. |
| **Test environment** | Same as Group A. |
| **Prerequisites** | If product definition checks only main diagonals, clarify whether anti-diagonal is in scope (source table includes it). |
| **Pass / fail criteria** | Returns `False` when anti-diagonal violates magic sum. |
| **Special procedures** | Align with domain definition (D5): both diagonals vs main only. |
| **Priority** | P1 |

---

## TC-MS-C-001

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-C-001 |
| **Test date** | |
| **Test purpose** | **Happy path:** complete a partially filled magic square by filling blanks so all rows, columns, and diagonals satisfy the magic property. |
| **Function under test** | `solution` (completion / solver entry point) |
| **Input / prerequisites** | Partially filled 4×4 grid with blanks in “standard” positions per source table (solvable case). |
| **Test steps** | 1. **Given** valid partial input.<br>2. **When** `solution` is executed.<br>3. **Then** output is a completed magic square (or equivalent success representation per API). |
| **Test environment** | Same as above; optional golden fixture. |
| **Prerequisites** | Input valid per product rules (size, range, blank count per contract). |
| **Pass / fail criteria** | Resulting grid is magic; blank cells filled correctly. **Fail:** wrong values, not magic, or wrong error. |
| **Special procedures** | None. |
| **Priority** | P1 |

---

## TC-MS-C-002

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-C-002 |
| **Test date** | |
| **Test purpose** | Verify completion for **different blank positions** than the standard case (still solvable). |
| **Function under test** | `solution` |
| **Input / prerequisites** | Partial matrix with blanks at alternate coordinates (still two blanks if following MagicSquare_01 contract). |
| **Test steps** | 1. **Given** alternate blank layout.<br>2. **When** `solution` runs.<br>3. **Then** valid completion matching magic rules. |
| **Test environment** | Same as TC-MS-C-001. |
| **Prerequisites** | Solvable instance for chosen positions. |
| **Pass / fail criteria** | Magic property holds; placements consistent with ordering policy (e.g. D6). |
| **Special procedures** | None. |
| **Priority** | P1 |

---

## TC-MS-C-003

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-C-003 |
| **Test date** | |
| **Test purpose** | **Boundary:** input is already a completed magic square — verify idempotent / no-op behavior (return same matrix or equivalent). |
| **Function under test** | `solution` |
| **Input / prerequisites** | Fully filled valid magic square (no blanks). |
| **Test steps** | 1. **Given** completed square.<br>2. **When** `solution` is called.<br>3. **Then** output equals input (or documented identity behavior). |
| **Test environment** | Same as TC-MS-C-001. |
| **Prerequisites** | No `0` cells; matrix already magic. |
| **Pass / fail criteria** | Returned structure matches input per equality rules. **Fail:** mutation when not allowed, or error. |
| **Special procedures** | **Remark:** boundary — no blanks. |
| **Priority** | P2 |

---

## TC-MS-C-004

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-C-004 |
| **Test date** | |
| **Test purpose** | **Boundary:** verify correct handling when minimum value **1** must appear in the solution. |
| **Function under test** | `solution` |
| **Input / prerequisites** | Case constructed so that `1` is among missing or critical placements (MIN = 1). |
| **Test steps** | 1. **Given** input where `1` is part of the valid completion.<br>2. **When** `solution` runs.<br>3. **Then** cell values include `1` in the correct position. |
| **Test environment** | Same as TC-MS-C-001. |
| **Prerequisites** | Legal partial board per domain. |
| **Pass / fail criteria** | Value `1` appears exactly once and in the correct cell per solution. |
| **Special procedures** | **Remark:** MIN = 1. |
| **Priority** | P2 |

---

## TC-MS-C-005

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-C-005 |
| **Test date** | |
| **Test purpose** | **Boundary:** verify correct handling when maximum value **16** must appear in the solution. |
| **Function under test** | `solution` |
| **Input / prerequisites** | Case where `16` is required in the completion (MAX = 16). |
| **Test steps** | 1. **Given** input involving `16`.<br>2. **When** `solution` runs.<br>3. **Then** `16` placed correctly once. |
| **Test environment** | Same as TC-MS-C-001. |
| **Prerequisites** | Valid range 1–16. |
| **Pass / fail criteria** | `16` present exactly once at expected coordinate. |
| **Special procedures** | **Remark:** MAX = 16. |
| **Priority** | P2 |

---

## TC-MS-C-006

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-C-006 |
| **Test date** | |
| **Test purpose** | During/after solution, verify **every row** sums to the magic constant **34**. |
| **Function under test** | `solution` (assertion on result) |
| **Input / prerequisites** | Solvable partial board per TC-MS-C-001 family. |
| **Test steps** | 1. **Given** valid input.<br>2. **When** `solution` completes.<br>3. **Then** each of the four row sums equals 34. |
| **Test environment** | pytest assertions on output matrix. |
| **Prerequisites** | Successful completion path. |
| **Pass / fail criteria** | All row sums == 34. |
| **Special procedures** | Part of magic constant verification trio (C-006–C-008). |
| **Priority** | P1 |

---

## TC-MS-C-007

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-C-007 |
| **Test date** | |
| **Test purpose** | Verify **every column** sums to **34** after solution. |
| **Function under test** | `solution` |
| **Input / prerequisites** | Same class as TC-MS-C-006. |
| **Test steps** | 1. **Given** valid input.<br>2. **When** solution produced.<br>3. **Then** all column sums == 34. |
| **Test environment** | Same as TC-MS-C-006. |
| **Prerequisites** | Successful completion. |
| **Pass / fail criteria** | All column sums == 34. |
| **Special procedures** | None. |
| **Priority** | P1 |

---

## TC-MS-C-008

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-C-008 |
| **Test date** | |
| **Test purpose** | Verify **both diagonals** sum to **34** after solution. |
| **Function under test** | `solution` |
| **Input / prerequisites** | Same class as TC-MS-C-006. |
| **Test steps** | 1. **Given** valid input.<br>2. **When** solution produced.<br>3. **Then** main and anti-diagonal sums == 34 per product definition. |
| **Test environment** | Same as TC-MS-C-006. |
| **Prerequisites** | Successful completion. |
| **Pass / fail criteria** | Diagonal sums == 34 as required by spec. |
| **Special procedures** | None. |
| **Priority** | P1 |

---

## TC-MS-D-001

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-D-001 |
| **Test date** | |
| **Test purpose** | **Error / validation:** out-of-range cell values (e.g. **17** or **-1**) are rejected or handled per API (no silent bad completion). |
| **Function under test** | `solution` / validation layer (boundary of public API) |
| **Input / prerequisites** | Matrix containing a value outside 1–16 (or outside allowed set including `0` for blanks). |
| **Test steps** | 1. **Given** invalid value in a cell.<br>2. **When** `solution` (or validator) runs.<br>3. **Then** `ValueError` **or** validation returns `False` per original spec wording. |
| **Test environment** | pytest `pytest.raises` or assert on return code. |
| **Prerequisites** | Invalid numeric range. |
| **Pass / fail criteria** | Expected exception or `False` as per contract; no completed magic square returned. |
| **Special procedures** | **Remark:** input validity. Align with `E_VALUE_RANGE` in MagicSquare_01. |
| **Priority** | P1 |

---

## TC-MS-D-002

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-D-002 |
| **Test date** | |
| **Test purpose** | **Duplicate values:** e.g. two **11**s — must not treat as valid partial board for completion. |
| **Function under test** | `solution` / duplicate check |
| **Input / prerequisites** | 4×4 matrix with duplicate non-zero values. |
| **Test steps** | 1. **Given** duplicate entries.<br>2. **When** `solution` runs.<br>3. **Then** returns `False` or raises per spec (source: `False`). |
| **Test environment** | Same as D-001. |
| **Prerequisites** | Duplicates among 1–16. |
| **Pass / fail criteria** | No successful magic completion; `False` or domain error as specified. |
| **Special procedures** | **Remark:** duplicate check. Maps to `E_DUPLICATE_VALUE`. |
| **Priority** | P1 |

---

## TC-MS-D-003

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-D-003 |
| **Test date** | |
| **Test purpose** | **Wrong size:** e.g. **3×3** matrix instead of required 4×4. |
| **Function under test** | `solution` / size validation |
| **Input / prerequisites** | Non-4×4 matrix. |
| **Test steps** | 1. **Given** 3×3 (or other wrong size).<br>2. **When** API invoked.<br>3. **Then** `ValueError` or `False` per source. |
| **Test environment** | Same as D-001. |
| **Prerequisites** | Dimension mismatch. |
| **Pass / fail criteria** | No completion; error or `False` as contract. |
| **Special procedures** | **Remark:** size check. Maps to `E_WRONG_SIZE`. |
| **Priority** | P1 |

---

## TC-MS-D-004

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-D-004 |
| **Test date** | |
| **Test purpose** | **`None`** or **empty** input must not proceed as normal matrix. |
| **Function under test** | `solution` / adapter |
| **Input / prerequisites** | `None` or `[]` passed where matrix expected. |
| **Test steps** | 1. **Given** null or empty input.<br>2. **When** function called.<br>3. **Then** `TypeError` (per source). |
| **Test environment** | pytest. |
| **Prerequisites** | None valid matrix. |
| **Pass / fail criteria** | `TypeError` raised (or project-mapped `E_NULL_INPUT` if using structured errors instead — document mapping). |
| **Special procedures** | Reconcile with MagicSquare_01: may use structured error instead of `TypeError`; update **Pass / fail** if so. |
| **Priority** | P1 |

---

## TC-MS-D-005

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-D-005 |
| **Test date** | |
| **Test purpose** | **Type check:** matrix contains a **string** (non-numeric) where number expected. |
| **Function under test** | `solution` / schema validation |
| **Input / prerequisites** | Nested structure with at least one `str` cell. |
| **Test steps** | 1. **Given** string in cell.<br>2. **When** API runs.<br>3. **Then** `TypeError` per source. |
| **Test environment** | Same as D-004. |
| **Prerequisites** | Invalid element type. |
| **Pass / fail criteria** | `TypeError` or equivalent validation failure; no bogus numeric coercion. |
| **Special procedures** | **Remark:** type check. |
| **Priority** | P2 |

---

## TC-MS-D-006

| Field | Value |
|--------|--------|
| **Test ID** | TC-MS-D-006 |
| **Test date** | |
| **Test purpose** | **Jagged / irregular rows:** outer list length 4 but inner rows have unequal lengths. |
| **Function under test** | `solution` / size validation |
| **Input / prerequisites** | “4×4” outer shape with ragged rows (e.g. lengths 4,3,4,4). |
| **Test steps** | 1. **Given** jagged matrix.<br>2. **When** validated.<br>3. **Then** `ValueError` per source. |
| **Test environment** | Same as D-001. |
| **Prerequisites** | Not a true 4×4 rectangular grid. |
| **Pass / fail criteria** | `ValueError` or `E_WRONG_SIZE`-equivalent; no completion. |
| **Special procedures** | None. |
| **Priority** | P2 |

---

## Traceability note

| Source group | IDs | Maps to README / Report (indicative) |
|--------------|-----|--------------------------------------|
| A — blanks | TC-MS-A-001 … A-005 | D7 blank order; blank count variants vs strict `E_BLANK_COUNT` |
| B — magic check | TC-MS-B-001 … B-005 | D5 / `isCompletedMagicSquare` |
| C — solution | TC-MS-C-001 … C-008 | D4/D6 completion, golden paths |
| D — errors | TC-MS-D-001 … D-006 | T-U / validation order, `E_*` codes |

Fill **Author**, **Approver**, **Created date**, **Test date**, and **Test organization** when you freeze the document.
