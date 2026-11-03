# Playwright Practical 7-Day Progress

**Plan:** `Playwright_Updated_Practical_7_Day_Plan.docx`  
**Rule:** Attempt first yourself → then ask for review/hints.

**How to use:** Change `[ ]` to `[x]` when done.

---

## Overall status

| Day | Focus | Status |
|-----|--------|--------|
| 1 | Setup, first test, locators and assertions | Complete |
| 2 | Reliable interactions, waits and debugging | Complete |
| 3 | Pytest structure, fixtures and test data | Complete |
| 4 | Page Object Model and maintainability | Complete |
| 5 | End-to-end mini project | Complete |
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

**Status:** `[x] Complete`  
**Date done:** 29-oct-2026  
**File:** `automation_Day02/Day02_script.py` (+ `DEBUG_NOTES.txt`)

### Hands-on tasks
- [x] Form happy path + at least two invalid-input cases
- [x] Web-first assertions (`to_be_visible`, `to_have_text`, `to_be_enabled`, etc.)
- [x] No fixed `time.sleep()`; use condition-based waits
- [x] Failing test in headed/debug mode; inspect trace or screenshot
- [x] Dialog / iframe / new tab only if the demo app requires it

### Daily deliverable
- [x] Small form suite with negative cases + one documented debug investigation

### Review notes (Day 2)
- A: Selenium web-form happy path — fill fields, submit, assert `Received!` + `Form submitted`.
- B: OrangeHRM wrong username → `Invalid credentials` (assertion timeout increased for slow demo).
- C: OrangeHRM empty password → `required` validation visible.
- D: Web-first drill — visible, value, checked, enabled, have_text/contain_text; no sleeps.
- E: Debug notes in `DEBUG_NOTES.txt` — flaky B due to late error message; fixed with longer expect timeout.
- Ready for Day 3.

---

## Day 3 — Pytest structure, fixtures and test data

**Status:** `[x] Complete`  
**Date done:** 02-nov-2026  
**Folder:** `automation_Day03/` (`tests/`, `conftest.py`, `test_data/users.json`, `pytest.ini`, `.env`)

### Hands-on tasks
- [x] Organize tests into `test_form.py` and `test_login.py` with descriptive names
- [x] Custom `login_page` fixture (setup via BASE_URL; earlier yield/teardown practiced)
- [x] `pytest.mark.parametrize` for valid and invalid login inputs
- [x] Smoke and regression markers registered in `pytest.ini` (form smoke; login marks need restore after JSON move)
- [x] Login rows in `test_data/users.json`; `BASE_URL` / `FORM_URL` from `.env` (gitignored)

### Daily deliverable
- [x] Structured suite with custom fixture, parametrized cases, markers, and external test data

### Review notes (Day 3)
- A: Split suite — form happy path + login negative cases; names describe the check.
- B: `login_page` fixture opens login and was practiced with `yield` + `clear_cookies`; current fixture uses `BASE_URL` and `return page` (teardown dropped — restore `yield` + cleanup before Day 4 if needed).
- C: One `test_login` with 4 parametrized rows; all passed.
- D: `smoke` / `regression` registered; `-m smoke` and `-m regression` demonstrated; run from `automation_Day03` so `pytest.ini` loads.
- E: `users.json` drives parametrize; `.env` has `BASE_URL` and `FORM_URL`; missing env → `pytest.fail`; full suite **5 passed**.
- Follow-up: after moving data to JSON, per-row smoke/regression marks on login were removed — add a `mark` field in JSON (or map expected → mark) so `-m smoke` still includes valid login.
- Ready for Day 4 (POM).

---

## Day 4 — Page Object Model and maintainability

**Status:** `[x] Complete`  
**Date started:** 02-nov-2026  
**Date done:** 03-nov-2026  
**Folder:** `automation_Day04/`

**Focus:** Purpose of POM, locators and page actions together, test intent and assertions stay in the test.

### Hands-on tasks
- [x] A: Create `LoginPage` with locators and simple methods
- [x] B: Refactor login tests to use `LoginPage` (no repeated locator/action sequence)
- [x] C: Create `FormPage` and use it from the form test
- [x] D: Keep POM simple — review naming, duplication, no base class / helper layer
- [x] E: Wire Day 3 fixtures, data, markers, and env into the POM suite

### Daily deliverable
- [x] Small suite using one or two page objects (no overengineering)

### Review notes (Day 4)
- A: `LoginPage` with locators in `__init__`, action methods, OrangeHRM URL via fixture/`BASE_URL`.
- B: Parametrized login through `LoginPage.login(...)`; assertions stay in the test.
- C: `FormPage` + smoke form test; `Received!` / `Form submitted` asserted in test.
- D: Notes in `conftest.py` on page object vs test; no base class.
- E: `login_page` fixture with `yield` + clear cookies; `.env` URLs; `users.json` marks drive smoke/regression (`2` smoke / `3` regression collected).
- Ready for Day 5.

### Review question
Can you explain what belongs in a page object versus a test?

---

## Day 5 — End-to-end mini project

**Status:** `[x] Complete`  
**Date started:** 03-nov-2026  
**Date done:** 03-nov-2026  
**Folder:** `automation_Day05/` (`scenarios.md`)

**Focus:** Choosing scenarios, priority, positive/negative paths, and keeping tests independent.

### Hands-on tasks
- [x] A: Choose one demo app for Days 5–7; write a short scenario list (8–10)
- [x] B: Prioritize and automate the top 5–7 scenarios (POM + fixtures + test data where useful)
- [x] C: Keep values in test data / env — not hard-coded throughout tests
- [x] D: Mark each scenario Automated vs Manual in the list
- [x] E: Be ready to explain coverage — why each automated scenario matters (notes in scenarios.md; tighten wording below)

### Daily deliverable
- [x] Working mini-project: scenario list + at least 5 useful automated tests

### Review notes (Day 5)
- A–D pass. Sauce Demo mini-project: 7 automated (TC-01–07), 3 manual (TC-08–10).
- E: coverage notes present; correct idea — fix facts: wrong **password** (not username), empty **username** (not password), and mention locked-out; manual cases are not “already tested,” just lower priority/time.
- Ready for Day 6 after local `pytest` green.

### Review question
Can you describe the test coverage and why each scenario matters?

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
