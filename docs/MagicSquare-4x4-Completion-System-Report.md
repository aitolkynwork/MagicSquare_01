# Magic Square 4×4 Completion System — Summary Report

**Project:** MagicSquare  
**Purpose:** Single-page summary of the **4×4 magic square completion** system as specified in this repository.  
**Date:** 2026-04-28  

---

## Provenance (canonical sources)

| Document | Role |
|----------|------|
| [docs/PDR.md](PDR.md) | Problem framing, dual-track UX + logic contract language, scenario mapping |
| [Report/01.problem-definition-report.md](../Report/01.problem-definition-report.md) | Problem definition steps 1–5, exclusions |
| [Report/02.layer-design-contracts-tdd-report.md](../Report/02.layer-design-contracts-tdd-report.md) | Fixed I/O contracts, domain invariants D1–D7, boundary errors, integration and coverage |
| [Report/04.user-journey-levels-1-5-report.md](../Report/04.user-journey-levels-1-5-report.md) | Epic through Level-4 technical scenarios |

This report **does not** replace those artifacts; it **aggregates** them for onboarding and planning.

---

## 1. Executive summary

The system accepts a **partially filled 4×4** grid representing a **normal** magic square instance (distinct integers **1–16**, magic sum **34**). **Exactly two** cells are empty, encoded as **0**. It **validates** structure and values, **computes** the two missing numbers and their placement order per a **deterministic policy**, and returns a **fixed-length numeric result** for callers. Invalid inputs and **unsolvable** or **ambiguous** (both placements valid) cases yield **named errors** with **stable messages**. The project prioritizes **layer separation**, **contract-first TDD**, and **traceability** over algorithmic novelty.

---

## 2. System boundary

**In scope:** Completion of a **single** puzzle instance under the stated arithmetic and indexing rules; optional **local persistence** of last input/result (see layer report).

**Out of scope (examples):** General board sizes; arbitrary value sets; multiple independent users; cloud sync; ML-driven completion (MLOps surfaces in the PDR apply only if ML is added later).

---

## 3. Domain rules (completion contract)

| Rule | Specification |
|------|----------------|
| Grid | **4×4** integers |
| Empty cell | **0** |
| Fill values | **1–16** where not empty |
| Blanks | **Exactly two** cells equal **0** |
| Uniqueness | No **duplicate** non-zero values |
| Magic property | Every **row**, **column**, and **both main diagonals** sums to **34** on the **completed** grid |
| multiset | Completed grid uses **each of 1…16 exactly once** |
| Solving | Infer the two missing values; if **both** assignments (smaller-first vs swapped to blanks) satisfy magic + multiset, treat as **ambiguous** (reject per design); if **neither**, **unsolvable** |
| Output | **`int[6]`**: `[r1, c1, n1, r2, c2, n2]` with **1-based** row/column indices; `(r1,c1)` then `(r2,c2)` follow **blank order** (row-major among zeros); `(n1, n2)` follow the **D6 ordering rule** (smaller to first blank first **if** that completion is magic; else reversed) |

---

## 4. External contracts (caller-facing)

**Input:** `int[][]` — **4** rows, each length **4**; cells **0** or **1–16**; exactly **two** zeros; fourteen non-zero values all **distinct**.

**Output (success):** `int[6]` as above.

**Errors (boundary schema):** Enumerated codes including `E_NULL_INPUT`, `E_WRONG_SIZE`, `E_VALUE_RANGE`, `E_BLANK_COUNT`, `E_DUPLICATE_VALUE`, `E_DOMAIN_UNSOLVABLE`, `E_DOMAIN_AMBIGUOUS`, `E_INTERNAL` (and optional storage corruption). **Literal messages** are fixed in [Report/02](../Report/02.layer-design-contracts-tdd-report.md) §2.4; **validation order** (null → size → range → blank count → duplicates) is part of the contract.

---

## 5. Architecture (ECB)

| Stereotype | Responsibility |
|--------------|----------------|
| **Entity (domain)** | `PartialMagicSquare` and rules **D1–D7**: dimensions, blanks, duplicates, missing pair, magic completeness (**34**), placement evaluation, output number ordering |
| **Control** | Orchestrates validate → solve → optional persistence; no duplicated arithmetic rules |
| **Boundary** | Input/output mapping, error mapping to codes and messages; **no** business rules beyond transport/schema checks as chosen per implementation policy |

Dependency direction: **domain** has no outward dependencies; **control** uses domain (+ data ports); **boundary** uses application/facade; **data adapters** implement ports (file/in-memory).

---

## 6. Key domain invariants (traceability IDs)

| ID | Short description |
|----|-------------------|
| D1 | 4×4 grid |
| D2 | Two zeros; other cells in 1–16 |
| D3 | Distinct non-zero values |
| D4 | Completed trial uses full 1…16 multiset |
| D5 | All lines sum to **34** |
| D6 | Output `(n1,n2)` from the two placement attempts |
| D7 | Blank order: lexicographic **1-based** row-major |

Use cases **UC-D1** … **UC-D5** in Report/02 map directly to tests and components in the traceability matrix (same document §4.5).

---

## 7. Verification and quality bar

- **Dual-track TDD:** boundary/contract tests (**T-U\***) and domain tests (**T-D\***) per Report/02; integration scenarios **T-I01–T-I05**; optional data tests **T-DS01–T-DS07**.
- **Coverage targets (indicative):** domain **≥95%** line; boundary **≥85%**; data **≥80%** (Report/02 §4.4).
- **Regression:** golden fixtures (e.g. solvable smaller-first, solvable reversed-only, unsolvable-with-valid-schema); frozen `int[6]` layout and message literals unless versioned.

---

## 8. User-facing narrative (condensed)

From [Report/04](../Report/04.user-journey-levels-1-5-report.md): the **epic** is an **invariant-based thinking** training path using this puzzle. Success means **clear contracts**, **separated domain logic**, **no magic numbers** in code (use **named constants**, e.g. **34**), and **traceability** from invariants to tests.

---

## 9. Related documents

- **Problem only (no build design):** Report/01, `docs/PDR.md`  
- **Build and test design:** Report/02  
- **Journey and scenarios:** Report/04  

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-28 | Initial summary report in `docs/` |
