# Playwright Practical 7-Day Progress

**Plan:** `Playwright_Updated_Practical_7_Day_Plan.docx`  
**Rule:** Attempt first yourself → then ask for review/hints.

**How to use:** Change `[ ]` to `[x]` when done.

---

## Overall status

| Day | Focus | Status |
|-----|--------|--------|
| 1 | Setup, first test, locators and assertions | Complete |
| 2 | Reliable interactions, waits and debugging | Not started |
| 3 | Pytest structure, fixtures and test data | Not started |
| 4 | Page Object Model and maintainability | Not started |
| 5 | End-to-end mini project | Not started |
| 6 | Stability, reporting and running the suite | Not started |
| 7 | Independent challenge, review and demo | Not started |

---

## Day 1 — Setup, first test, locators and assertions

**Status:** `[x] Complete`  
**Date done:** 28-oct-2026  
**File:** `automation_Day01/first_test.py`

### Hands-on tasks
- [x] Set up project and install pytest-playwright; browsers available
- [x] Create and run tests that open a demo app and verify title/heading
- [x] Practise `get_by_role`, `get_by_label`, `get_by_text`, `get_by_placeholder`, and `locator()`
- [x] Automate a form field and button; verify visible results
- [x] Intentionally break one locator and observe the failure (`TimeoutError` on `Submit123`)

### Daily deliverable
- [x] Runnable test file with at least 3 tests and clear assertions (A–D pass)

### Review notes (Day 1)
- A: title check on Selenium web form.
- B: Demo Web Shop title + heading visible.
- C: locator drill on Sauce demo (role, text, placeholder, label).
- D: fill text field, assert value, Submit, assert `#message` = `Received!`.
- E: broken locator `Submit123` → `Locator.click: Timeout 30000ms exceeded` (learning only; remove or fix before Day 2 so the suite is green).
- Ready for Day 2.

---

## Day 2 — Reliable interactions, waits and debugging

**Status:** `[ ] Not started`  
**Date done:**  
**File:**

### Hands-on tasks
- [ ] Form happy path + at least two invalid-input cases
- [ ] Web-first assertions (`to_be_visible`, `to_have_text`, `to_be_enabled`, etc.)
- [ ] No fixed `time.sleep()`; use condition-based waits
- [ ] Failing test in headed/debug mode; inspect trace or screenshot
- [ ] Dialog / iframe / new tab only if the demo app requires it

### Daily deliverable
- [ ] Small form suite with negative cases + one documented debug investigation

---

## Day 3 — Pytest structure, fixtures and test data

**Status:** `[ ] Not started`

### Daily deliverable
- [ ] Structured suite with one custom fixture, parametrize, and markers

---

## Day 4 — Page Object Model and maintainability

**Status:** `[ ] Not started`

### Daily deliverable
- [ ] Small suite using one or two page objects (no overengineering)

---

## Day 5 — End-to-end mini project

**Status:** `[ ] Not started`

### Daily deliverable
- [ ] Scenario list + at least 5 useful automated tests

---

## Day 6 — Stability, reporting and running the suite

**Status:** `[ ] Not started`

### Daily deliverable
- [ ] Repeatable suite, HTML report, README

---

## Day 7 — Independent challenge, review and demo

**Status:** `[ ] Not started`

### Daily deliverable
- [ ] Demo of mini-project + short self-review
