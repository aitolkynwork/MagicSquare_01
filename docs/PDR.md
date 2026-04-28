# Problem Definition Report (PDR)

**Project:** MagicSquare  
**Subject:** 4×4 magic square — problem recognition and definition

This file is the canonical **Problem Definition Report** in the `docs/` tree.

## Provenance

| Artifact | Role |
|----------|------|
| [Report/01.problem-definition-report.md](../Report/01.problem-definition-report.md) | Structured report (Steps 1–5), exclusions, and document map |
| [Prompting/01.problem-definition-report-prompt.md](../Prompting/01.problem-definition-report-prompt.md) | Elicitation steps and Q&A that produced the report narrative |

The narrative in **§§1–5** aligns with the authoritative report in [Report/01.problem-definition-report.md](../Report/01.problem-definition-report.md). Sections **Reading frame** through **Scenario mapping (illustrative)** are additions to this PDR: they restate the same problem using **dual-track UI + logic** vocabulary and an **MLOps contract-surface** lens for later verification traceability. They do not change Report/01 and are not a substitute for layer design in [Report/02.layer-design-contracts-tdd-report.md](../Report/02.layer-design-contracts-tdd-report.md).

---

**Scope of this document:** Problem recognition and definition, including **named contract surfaces** that a solution will later need to honor: observable **UX outcomes**, **logic rules** / invariants, and (when machine learning is in scope) **data and model policy** at the level of outcomes and gates—not tooling or stack choices.

**Excluded by intent:** Implementation design, any algorithmic approach, and any discussion of how a solution would be built technically (frameworks, services, pipeline products).

---

## Document map

| Section | Source (Step) | UI track | Logic track | MLOps track |
|--------|---------------|----------|-------------|-------------|
| [Reading frame](#reading-frame-dual-track-ui-logic-tdd-and-mlops) | PDR extension | ● | ● | ● |
| [Cross-track mapping](#cross-track-mapping-of-sections-1-to-5) | PDR extension | ● | ● | ● |
| [MLOps lens](#mlops-lens-problem-level-contract-surfaces) | PDR extension | ○ | ○ | ● |
| [Scenario mapping](#scenario-mapping-illustrative) | PDR extension | ● | ● | ● |
| [1. Observation](#1-observation) | Step 1 | ○ | ● | ○ |
| [2. Why completion matters](#2-why-completion-matters) | Step 2 | ● | ● | ○ |
| [3. Why a program versus manual calculation](#3-why-a-program-versus-manual-calculation) | Step 3 | ○ | ● | ○ |
| [4. Why specification-first discipline](#4-why-specification-first-discipline) | Step 4 | ● | ● | ● |
| [5. True problem definition](#5-true-problem-definition) | Step 5 | ● | ● | ○ |

Legend: **●** = primary emphasis in that section; **○** = secondary or optional (MLOps only when ML participates).

---

## Reading frame: Dual-track UI, logic TDD, and MLOps

**Dual-track verification (conceptual):** The problem can be read through two coupled tracks that later drive TDD:

- **UI track (boundary):** What users or integrators **observe**—visibility, possibility, activation, inclusion of messaging or affordances—summarized as a **UX contract** (for example: no error before input; a named error when a named failure applies).
- **Logic track (domain):** What must **hold** regardless of presentation—summarized as **logic rules** (allow/reject, maintain/suspend, return/block, calculate/save at the problem level).

**MLOps (when machine learning is on the path):** The same “named outcomes” idea extends to **data validity**, **versioned model behavior**, **evaluation and promotion gates**, and **reproducibility** (lineage, thresholds as policy). At PDR depth this means **contract surfaces**: what “correct” must mean across retrains and deployments—not a prescription for specific MLOps products or code layout.

**TDD rhythm (philosophy only):** *UI creates RED from design (UX contract); logic—and, where relevant, ML gates—creates RED from rules and evidence.* **GREEN** and **REFACTOR** are shared concerns: behavior stays checkable without collapsing boundary tests into domain tests or the reverse.

### UX contract language and logic rule language

Two controlled vocabularies help scenarios become **decisions** that can later become tests. Prefer items that express a **decision** or **state change**, not vague to-dos.

| UX contract language (observable) | Logic rule language (decision) |
|-----------------------------------|--------------------------------|
| Visible / not visible | Allow / reject |
| Possible / impossible | Maintain / suspend |
| Activated / deactivated | Return / block |
| Included / not included | Calculate / save |

---

## Cross-track mapping of sections 1 to 5

| Section | Step | UI track (boundary) | Logic track (domain) | MLOps track |
|---------|------|---------------------|----------------------|-------------|
| §1 Observation | 1 | Contexts and outcomes stakeholders see or teach | Constrained assignment; reliable outcomes | N/A for a purely combinatorial core; “invalid batch/schema” when ML assists |
| §2 Why completion matters | 2 | Avoid misleading partial success; clarify impossible vs many solutions | Partial vs global consistency; unsat; uniqueness | Policy when model-assisted completion is uncertain or contradicted by rules |
| §3 Program vs manual | 3 | — | Repeatability; mechanical verification | Repeatable runs; logged eval artifacts when models exist |
| §4 Specification-first | 4 | I/O boundaries; named failures users can see | Rules, invariants, determinism | Reproducibility; thresholds; named gate failures |
| §5 True problem definition | 5 | Surface vs misleading “success” in the UI | Accurate definition; domain invariants | Behavior stable under declared data/model policy |

---

## MLOps lens (problem-level contract surfaces)

When an ML component participates (for example ranking hints or parsing sketches), the problem definition should still name, **without implementation detail**:

- **Data contract** — Valid inputs; what invalid or out-of-distribution means for the product story.
- **Evidence** — What measured behavior must hold before a change is trusted, stated as **policy** (for example holdout criteria), not as ad hoc tuning steps.
- **Lineage** — “The same problem” includes the same declared rules **and** the same declared data/model policy wherever ML affects outcomes.
- **Failure parity** — Logic **reject** or **block** outcomes have **observable** UX counterparts; automated gate failures align with those semantics.

For a **pure** deterministic magic-square artifact with **no** ML, the MLOps column is **not applicable**; the rows above keep the slot for combined products.

---

## Scenario mapping (illustrative)

Illustrative rows connecting **scenario → UX contract → logic rule → ML / ops gate** (last column relevant only when ML or batch pipelines exist).

| Scenario | UX contract | Logic rule | ML / ops gate (if ML in scope) |
|----------|-------------|------------|--------------------------------|
| No ruling yet before the user finishes a defined input step | Inappropriate error messaging **not visible** | No premature **reject** if partial semantics allow an intermediate state | Model-driven blocking **not** applied before required inputs/features exist |
| Completed grid violates the agreed line-sum / distinctness rules | Named invalid or error state **visible** | Magic rule set **rejects** that candidate | Shadow or offline **eval** records disagreement with the deterministic checker |
| Structural puzzle rule violated (for example wrong count of empty cells) | Named structural error **visible** | Completion **suspended** or input **blocked** | Schema or row validation **rejects** batch; promotion **blocked** |
| Cell value not an allowed integer in range | Invalid styling or message **visible** | Input **blocked** at boundary | Parser **rejects**; pipeline **blocks** until fixed |
| Correct completion under all declared rules | Success state **visible** | Valid result **returned** per policy | Optional: model agrees with checker on golden set before release |

---

## 1. Observation

### 1.1 Situation being addressed

The situation is a **need concerning a 4×4 grid of numbers** under a strict balance rule: each full row, each full column, and both main diagonals must sum to the **same total**, with cells typically expected to use a **fixed set of distinct values** (often the integers from 1 through 16). The concrete need may present as: an empty grid to be filled legally; a partially filled grid to be completed or corrected; a filled grid whose correctness must be judged; or a need to **explain or catalogue** how such arrangements arise. The situation is defined by **constrained assignment on sixteen positions** and the need for **reliable outcomes** (existence, one example, many examples, or verification)—not by the label “magic square” alone.

### 1.2 Why this problem is worth addressing

At 4×4 the instance is **small enough to reason about manually** yet **rich enough to show real structure**: once the value set is fixed, the magic total is determined; not every naive filling works; symmetries and classical constructions become teachable; and systematic exploration remains tractable in many settings compared with larger boards. It occupies a **useful demo size** between trivial smaller cases and explosive larger ones.

### 1.3 Contexts where the problem appears

**Learning:** Discrete mathematics and recreational mathematics (definitions, counting, symmetry); introductory systematic methods; constraint-style reasoning; exercises that reward clear definitions and edge-case thinking; connections to history or famous examples.

**Broader systems thinking:** Rarely as a standalone production feature, but the **pattern**—assigning values under overlapping sum constraints—appears wherever balanced assignments, puzzle engines, educational tools, or small combinatorial checks matter. The 4×4 case is a **compact specimen** of that class.

---

## 2. Why completion matters

### 2.1 Assumed rationale

**Completion is required because the situation only “counts” when every cell is filled and every required line can be evaluated together.** The stakeholder’s goal is a **fully specified 4×4 assignment**, not a fragment—whether for a puzzle answer, a demonstration artifact, or a certificate that the constraints can be satisfied simultaneously.

### 2.2 Structural issues and inconveniences that assumption exposes

1. **“Complete” bundles several different tasks** — filling from scratch, repairing a broken grid, or extending a partial assignment that is already consistent on some lines. Each has different failure modes (no solution, many solutions, dead ends).

2. **Partial grids can mislead** — Some fillings look locally plausible yet are **globally impossible** once remaining lines are considered. If completion is the only goal, **early feedback** on correctness remains weak unless partial states are given a defined meaning.

3. **Completion presumes satisfiability** — The request may be **unsatisfiable**. The structure then demands an explicit policy: report impossibility, relax rules, or change the value set.

4. **Uniqueness is not implied** — Multiple valid completions may exist. “Must complete” does not decide whether one answer or many is required, or whether symmetric variants should be treated as distinct.

5. **Process versus artifact** — If the motive is “only the finished grid shows the property,” tension appears with **valuing the reasoning path** (hints, steps, justification).

6. **Scope of “valid” may grow** — A completed grid invites checks beyond what was first named (extra line families, variant definitions). The rule family must be **fixed** or creep becomes a specification risk.

7. **Fixed value domain** — “Complete the magic square” often silently assumes a fixed set of values. If that set is negotiable, the real driver may be “find **some** admissible assignment under **these** rules,” which is a different framing.

**Net:** “Completion” forces clarity on **partial-state semantics**, **impossibility handling**, **choice among completions**, and the **exact line family and value domain**.

---

## 3. Why a program versus manual calculation

*Here “manual calculation” means doing arithmetic and filling or checking a grid by hand, on paper, or in an informal scratch workspace without a fixed, repeatable procedure.*

### 3.1 Repeatability

A program **fixes inputs, procedure, and outputs** so the same problem class can be re-run under the same rules. Manual work drifts with **fatigue, notation, and memory of a particular construction**. Repeatability supports **many trials**, **comparison after a change**, and **sharing** a method without depending on who was present for the original scratch work.

### 3.2 Automated verification

Manual work typically yields a **candidate**; correctness still requires **re-checking every line and distinctness**, which scales poorly and invites shortcuts. A program can **hold the rule set in one place** and apply it mechanically to any candidate (complete or partial, if partial checking is defined). **Construction** and **judgment** separate cleanly.

### 3.3 Error prevention

People transpose digits, disturb one cell while the rest “look” balanced, mis-sum diagonals, or **drop a constraint** after a long chain of edits. A defined procedure shifts residual risk toward **errors in the written specification** of the procedure itself—often **localizable and revisable**—and reduces **silent wrong answers** that still feel like success.

### 3.4 Rule-based thinking practice

Specifying a procedure with precision forces **explicit rules**: which lines count, which values are allowed, what “complete” means, what to deliver when no completion exists. Manual solving often leaves those rules **implicit**. Making constraints **named and ordered** is practice in **rule-based thinking**: stating states, branches, and falsifiable outcomes.

**Synthesis:** Manual calculation suits **one-off insight or a remembered pattern**. A program suits **reliability**, **mechanical checking**, **fewer undetected slips**, and **making the rule system explicit enough to disagree with constructively**.

---

## 4. Why specification-first discipline

*This section restates the chat’s “TDD” insight in problem-definition terms: driving the work from **checkable statements of correct behavior** before elaborating internal mechanics.*

### 4.1 What must be controlled

- **The rule set** — Which lines must share a sum, allowed values, distinctness, and whether “magic” includes only those lines or a wider family. Drift between different parts of the work yields **inconsistent construction and judgment**.

- **Determinism where it matters** — Ordering of multiple solutions, tie-breaking, any stochastic element and its seeding policy.

- **Failure semantics** — No solution, invalid input, partial input if allowed. Each needs a **named outcome**, not an accidental default.

- **Scope boundaries** — Fixed 4×4 versus parameterized size; fixed value set versus configurable. These choices change what “correct” means.

### 4.2 Invariants (discipline-oriented)

- **Shape and domain** — Sixteen positions; values from the declared domain when “complete.”

- **Distinctness** (when required by the model) — No duplicated values.

- **Uniform line sum** — Every line in the agreed family sums to the **same** magic constant for that model.

- **Semantic alignment** — The constant implied by the rules **matches** every required line sum.

- **Coherence of judgment** — Anything labeled valid satisfies **every** stated rule; invalidity is supported by a **specific violated rule**.

- **Reproducibility under policy** — Same inputs and same documented freedom (e.g. ordering policy) yield documented, repeatable outcomes.

### 4.3 Why clear input and output boundaries matter

- **Checkability** — Ambiguous boundaries produce **brittle or subjective** success (“looks right”).

- **Separation of concerns** — Reading a grid, judging it, and presenting a result can be reasoned about **independently** when each boundary is explicit.

- **Specification creep** — Fuzzy boundaries hide new requirements. Clear contracts make change **visible**: a new requirement becomes a **new stated case**, not tacit behavior.

- **Communication** — Others (and your future self) can **audit** the stated cases: valid square, broken diagonal, wrong constant, duplicate value, wrong size.

**Key insight:** A magic square is a **finite specification problem** with many crisp properties and edge cases. Specification-first discipline **anchors what “correct” means** while internal approach remains free. Without controlled rules, clear boundaries, and stated invariants, “success” can mean **running without error** while **“magic” no longer matches the intended meaning**.

---

## 5. True problem definition

### 5.1 Surface definition (misleadingly narrow)

“Deliver something that prints a 4×4 magic square” or “place 1–16 so rows, columns, and diagonals sum to 34.”

This **collapses distinct problems** (generate, complete from clues, verify user-provided grids, enumerate). It often **does not fix** which diagonals or lines count, what happens when **no solution** exists, or how **multiple solutions** are handled. Success can be mimicked with a **memorized example** or an **incorrect checker** while the real reliability and learning goals stay unstated. The flaw is **under-specification**, not necessarily false arithmetic.

### 5.2 Improved definition (accurate)

A **small, trustworthy artifact or process** is required that realizes a **named constraint model** on a 4×4 board: a fixed set of distinct values (typically integers 1–16) in sixteen cells such that **every line in an agreed family** (at minimum: four rows, four columns, two main diagonals) sums to the **same constant**, with that constant **following from the rules** rather than being chosen ad hoc. The work must declare how it supports **at least one** of: producing a satisfying assignment, rejecting or handling impossible inputs, and **mechanically verifying** a candidate—together with **explicit behavior** for valid input, invalid input, and unsatisfiable cases. The real object of work is **encoding and honoring a contract** (rules, boundaries, outcomes), not merely displaying a familiar grid.

### 5.3 Core invariants of the problem (domain-level)

| Category | Invariant (conceptual) |
|----------|-------------------------|
| Structure | A 4×4 assignment; when complete, all sixteen positions filled. |
| Distinctness | If the model is “normal,” all values distinct within the declared set. |
| Line sums | Every line in the magic family equals the **same** magic constant. |
| Alignment | That constant is the one implied by the value set and rules—no “almost” totals. |
| Judgment | Validity and invalidity align with the **full** stated rule list. |
| Policy | Where required, outcomes are reproducible under the documented policy. |

### 5.4 Thinking skills actually being trained

- **Specification discipline** — Replacing intuition with an **enumerable list of constraints** and edge cases.

- **Constraint reasoning** — Treating rows, columns, and diagonals as **overlapping balance conditions**; distinguishing local from global consistency.

- **Separation of construction and judgment** — Producing candidates versus **independently** validating them.

- **Failure-mode thinking** — Designing for **no solution**, **many solutions**, and **malformed input**, not only the success path.

- **Accountability** — Preferring **checkable claims** over one-off manual re-verification.

- **Explicit boundaries** — Making inputs, outputs, and error outcomes **unambiguous** so correctness is **observable**.

**Closing synthesis:** The thread from observation through specification discipline converges on one aim: **turn a familiar puzzle into a small, falsifiable theory of behavior**—stated rules, stated boundaries, and stated outcomes—before any concern for internal mechanics.

---

## Chat scope summary

| Step | Focus | UI track | Logic track | MLOps |
|------|--------|----------|---------------|-------|
| 1 | Observational framing: constrained 4×4 assignment, why 4×4, learning and applied contexts. | Contexts / teachable outcomes | Assignment structure, reliability | N/A unless ML-assisted |
| 2 | Why “completion” is assumed; what that assumption forces you to clarify. | Honest failure and ambiguity UX | Partial vs global, unsat, uniqueness | Uncertainty policy if ML assists |
| 3 | Why a repeatable, verifiable procedure beats informal calculation (four lenses). | — | Repeatability, verification | Artifact repeatability |
| 4 | Why drive from checkable behavior first: control, invariants, clear I/O. | Observable failures, boundaries | Rules, invariants, determinism | Gates, reproducibility |
| 5 | Surface vs accurate definition; domain invariants; skills trained. | Misleading “success” vs clear UX | Accurate definition, invariants | Stable policy where ML applies |

---

*End of Problem Definition Report.*
