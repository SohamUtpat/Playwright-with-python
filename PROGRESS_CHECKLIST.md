# Python + Playwright — 60-Day Progress Checklist

**Learner:** Soham  
**Start date:** 26 October 2026  
**Rule:** Attempt first yourself ? then ask for review/hints. Do not paste AI solutions as your own work.

**How to use:** Change `[ ]` to `[x]` when done. Update the **Status** line under each day.

---

## Overall status

| Phase | Days | Status |
|-------|------|--------|
| Python fundamentals | 01–15 | Complete |
| Playwright basics | 16–30 | Not started |
| Pytest + framework skills | 31–50 | Not started |
| Final project + CI | 51–60 | Not started |

---

## Day 01 — Setup and first Python program

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day01/first_python_program.py`

### Concepts
- [x] Python installed and `python --version` works
- [x] `pip --version` works (no space: `pip --version`)
- [x] Create a `.py` file and run it from the terminal
- [x] Variables (string assignment with `=`)
- [x] `print()` with labels
- [x] Comments (`#`)
- [x] Store and print a date as text

### Practice deliverable
- [x] Script prints name, role, learning goal
- [x] Script prints today's date
- [x] Ran successfully in terminal

### Review notes (Day 01)
- Good structure: clear variable names, labels, comment, date.
- Tiny tip: use a normal apostrophe in `Today's` (`'`) instead of a backtick (`` ` ``). Both may display, but `'` is the correct character in English text.
- Ready for Day 02.

---

## Day 02 — Variables and data types

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day02/Day2_script.py`

### Concepts
- [x] Strings
- [x] Integers
- [x] Floats
- [x] Booleans
- [x] Type conversion (`int()`, `str()`, `float()`, `bool()`)
- [x] `type()`
- [x] f-strings

### Practice deliverable
- [x] Test-case summary printer (id, name, status, duration — mix of types)

### Review notes (Day 02)
- A/C/D/E solid; report shows 3 cases + 66.67% pass rate.
- B lesson learned: `bool("")` is False; non-empty strings are True.
- Reminder: print after each case before variables are overwritten; `:.2f` formats floats.
- Prefer writing D yourself next time; AI code is for unblocking + explanation.

---

## Day 03 — Operators and comparisons

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day03/Day3_script.py`

### Concepts
- [x] Arithmetic operators
- [x] Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- [x] Logical operators (`and`, `or`, `not`)

### Practice deliverable
- [x] Decide pass/fail for sample test results using operators

### Review notes (Day 03)
- A/B/D/E solid; D correctly uses `==` and `<=` with `and` for pass rules.
- Small fixes: D print labels all say "Test case 1"; C missing full login rule with `and` + `not`.
- Good habit: section headers in output make review easy.

### Review notes (Day 04)
- A/B/C/E pass. D fixed: `elif account_locked` is correct.
- Optional improvement: check locked first, then username, then password, else grant — matches Q3 insight.
- Tip: change inputs once each to prove all four D messages in the terminal.

---

## Day 04 — Conditions

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day04/Day4_script.py`

### Concepts
- [x] `if` / `elif` / `else`

### Practice deliverable
- [x] Valid login / invalid login / password validation scenarios

---

## Day 05 — Loops

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day05/Day5_script.py`

### Concepts
- [x] `for` loops
- [x] `while` loops

### Practice deliverable
- [x] Process a list of test cases and print pass/fail

### Review notes (Day 05)
- A–D pass. D fixed: one index loop with `tests[i]` / `statuses[i]`.
- Minor: `count = 1` before A’s for-loop is unused; semicolons after `passed = 0;` are optional in Python.
- Going forward: no Assignment E (self-check Q&A) — code practice only.

---

## Day 06 — Lists and tuples

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day06/Day6_script.py`

### Concepts
- [x] Lists (add, remove, search, slice, iterate)
- [x] Tuples

### Practice deliverable
- [x] Store and work with test data in lists/tuples

### Review notes (Day 06)
- A–C pass. D counts fixed with `test_data[i][2]`.
- Skipped stretch: building a `failed_names` list with `.append` — revisit anytime.
- Key lesson: list index = item; string index = character; tuple index = field.

---

## Day 07 — Dictionaries and sets

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day07/Day7_script.py`

### Concepts
- [x] Dictionaries
- [x] Sets / removing duplicates

### Practice deliverable
- [x] User details as dict; unique usernames with a set

### Review notes (Day 07)
- A–D pass. Dict create/update/delete + loop over test statuses.
- Sets used to remove duplicate usernames.
- Revisit tonight: write set/dict from memory without looking.

---

## Day 08 — Functions

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day08/Day8_script.py`

### Concepts
- [x] Defining functions
- [x] Arguments / return values

### Practice deliverable
- [x] Reusable helpers for validation / formatting test results

### Review notes (Day 08)
- A–D pass. `validate_login`, string checks, `format_result` used in a loop.
- Revisit tonight: write one function from blank (args + return).

---

## Day 09 — Exceptions and files

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day09/Day9_script.py` (+ `test_data.txt`, `test_data.json`)

### Concepts
- [x] `try` / `except`
- [x] Reading text or JSON files

### Practice deliverable
- [x] Read test data; handle missing/invalid files

### Review notes (Day 09)
- A–D pass. Handles ValueError, FileNotFoundError, JSONDecodeError.
- Run from `Day09` folder so relative file paths work.
- Revisit tonight: open/read a file yourself and break it on purpose.

---

## Day 10 — Revision checkpoint 1

**Status:** `[x] Complete`  
**Date done:** 26-oct-2026  
**File:** `python language/Day10/Day10_script.py`

### Checkpoint (must explain without copying a full solution)
- [x] Variables
- [x] Conditions
- [x] Loops
- [x] Functions
- [x] Exceptions
- [x] Small CLI test-data utility built by you
- [x] Weak topics written down

### Review notes (Day 10)
- Utility: add / show / count test cases; file load with try/except.
- Weak topics noted: sets, JSON files, writing functions from blank.
- Tonight redo Days 07–10 yourself so the checklist stays honest.

---

## Days 11–15 — Python deeper + mini-project (prep for automation)

> Playwright / browser automation starts on **Day 16**. Days 11–15 finish the Python skills you will reuse in every test (modules, classes, JSON data, validation).

---

## Day 11 — Modules, packages, pip, venv

**Status:** `[x] Complete`  
**Date done:** 28-oct-2026  
**Files:** `python language/Day11/Day11_script.py`, `python language/Day11/test_data.py`, `python language/Day11/helpers.py`

### Concepts
- [x] Importing built-in modules (`math`, `datetime`, etc.)
- [x] Creating your own modules and importing them
- [x] Creating a virtual environment (`python -m venv .venv`)
- [x] Activating venv and using `pip install` / `pip list` / `pip freeze`

### Practice deliverable
- [x] Assignment A: use one built-in module
- [x] Assignment B: import data from `test_data.py`
- [x] Assignment C: import helpers from `helpers.py`
- [x] Assignment D: create venv, install a package (e.g. `requests`), note it in the script

### Review notes (Day 11)
- A–C pass. Own modules `test_data` + `helpers` imported and used.
- D: project `.venv` created; `requests` installed; `requirements.txt` frozen.
- Tip: run Day11 with `.venv\Scripts\python.exe` to see the requests version print.

---

## Day 12 — OOP basics

**Status:** `[x] Complete`  
**Date done:** 28-oct-2026  
**File:** `python language/Day12/Day12_script.py`

### Concepts
- [x] Class vs instance
- [x] Instance attributes
- [x] Instance methods
- [x] Working with a list of objects

### Practice deliverable
- [x] `User` class with attributes and methods
- [x] Multiple users created and explained
- [x] Loop over users (e.g. only active ones)

### Review notes (Day 12)
- A–D pass. `describe()` / `deactivate()` used; active users filtered in a loop.
- Revisit: explain class vs instance in your own words.

---

## Day 13 — Classes, methods, and `__init__`

**Status:** `[x] Complete`  
**Date done:** 28-oct-2026  
**File:** `python language/Day13/Day13_script.py`

### Concepts
- [x] `__init__` constructors
- [x] Instance attributes set in `__init__`
- [x] Methods that use `self`
- [x] Simple validation method on a class

### Practice deliverable
- [x] `LoginData` / `User` with `__init__`
- [x] `TestCase` class with `summary()`
- [x] Count pass/fail from a list of `TestCase` objects

### Review notes (Day 13)
- A–D pass. `LoginData.is_valid()` + `TestCase.summary()` + pass/fail counts.
- Revisit: write one class with `__init__` from blank.

---

## Day 14 — JSON and test data

**Status:** `[x] Complete`  
**Date done:** 28-oct-2026  
**Files:** `python language/Day14/Day14_script.py`, `python language/Day14/login_data.json`

### Concepts
- [x] `json.load` / `json.loads`
- [x] Iterating JSON records
- [x] Comparing computed validation vs expected field
- [x] `FileNotFoundError` and `json.JSONDecodeError`

### Practice deliverable
- [x] Load `login_data.json` and print records
- [x] Validate each login and match against `expected`
- [x] Handle missing file and invalid JSON

### Review notes (Day 14)
- A–D pass. All expected vs result checks PASS; missing file + bad JSON handled.
- Run from `Day14` folder so `login_data.json` is found.

---

## Day 15 — Python mini-project (test-data validator)

**Status:** `[x] Complete`  
**Date done:** 28-oct-2026  
**Files:** `python language/Day15/Day15_script.py`, `python language/Day15/validator.py`, `python language/Day15/loader.py`, `python language/Day15/sample_data.json`

### Concepts
- [x] Combine functions + modules + JSON + exceptions
- [x] Clear report-style output
- [x] Build without pasting a full AI solution

### Practice deliverable
- [x] Load JSON via `loader.py`
- [x] Validate records via `validator.py`
- [x] Print OK / INVALID lines + summary counts
- [x] Demo missing-file handling

### Review notes (Day 15)
- A–D pass. Report: total 5 | valid 2 | invalid 3; missing file returns None.
- Modules split cleanly: loader + validator + main script.
- Next: Day 16 — Install Playwright + Pytest (automation starts).

---

## Days 16–30 — Playwright basics

| Day | Topic | Done |
|-----|--------|------|
| 16 | Install Playwright + Pytest | [ ] |
| 17 | First browser test | [ ] |
| 18 | Locators | [ ] |
| 19 | Actions and assertions | [ ] |
| 20 | Navigation and browser state | [ ] |
| 21 | Waits and reliability | [ ] |
| 22 | Forms and validation | [ ] |
| 23 | Dialogs and alerts | [ ] |
| 24 | Dropdowns, tables, filters | [ ] |
| 25 | Tabs, windows, frames | [ ] |
| 26 | Screenshots, traces, debugging | [ ] |
| 27 | Uploads / downloads | [ ] |
| 28 | Cross-browser execution | [ ] |
| 29 | Test organization and naming | [ ] |
| 30 | Checkpoint 2 — mini suite (=8 tests) | [ ] |

---

## Days 31–50 — Pytest + framework

| Day | Topic | Done |
|-----|--------|------|
| 31 | Pytest fundamentals | [ ] |
| 32 | Fixtures | [ ] |
| 33 | Fixture scope and teardown | [ ] |
| 34 | Parametrization | [ ] |
| 35 | Markers and selective runs | [ ] |
| 36 | Configuration | [ ] |
| 37 | Environment variables / secrets | [ ] |
| 38 | Test data management | [ ] |
| 39 | Reporting | [ ] |
| 40 | Checkpoint 3 — stable suite | [ ] |
| 41 | Page Object Model (POM) | [ ] |
| 42 | POM for multiple pages | [ ] |
| 43 | Base page / helpers | [ ] |
| 44 | Project configuration | [ ] |
| 45 | Logging and failure evidence | [ ] |
| 46 | API testing basics (GET) | [ ] |
| 47 | API POST and test data | [ ] |
| 48 | UI + API together | [ ] |
| 49 | Git basics | [ ] |
| 50 | Checkpoint 4 — framework review | [ ] |

---

## Days 51–60 — Final project

| Day | Topic | Done |
|-----|--------|------|
| 51 | Project planning (10–15 scenarios) | [ ] |
| 52 | Implement core tests | [ ] |
| 53 | Expand coverage | [ ] |
| 54 | Reliability and debugging | [ ] |
| 55 | Cross-browser + config | [ ] |
| 56 | Reports and documentation | [ ] |
| 57 | CI/CD introduction | [ ] |
| 58 | Independent coding challenge | [ ] |
| 59 | Mock interview / explanation | [ ] |
| 60 | Final review and demonstration | [ ] |

---

## Weekly review (fill each week)

**Week of:** _______________

- [ ] Can I explain the concept without notes?
- [ ] Can I write a small example without a full copy-paste solution?
- [ ] Can I debug a simple failure and explain the cause?
- [ ] Did I save/commit working code and note open questions?
- [ ] Did I use Cursor to understand/review — not to replace learning?

**This week’s wins:**  
**Stuck on:**  
**Next focus:**  

---

## Progress log (newest on top)

| Date | Day | What I did | Result |
|------|-----|------------|--------|
| 28-oct-2026 | 15 | Day15 mini-project — loader + validator + JSON report | Pass |
| 28-oct-2026 | 14 | Day14_script.py — JSON logins, expected checks, exceptions | Pass |
| 28-oct-2026 | 13 | Day13_script.py — LoginData/TestCase, __init__, counts | Pass |
| 28-oct-2026 | 12 | Day12_script.py — User class, methods, active-user loop | Pass |
| 28-oct-2026 | 11 | Day11 modules + helpers/test_data; .venv + requests | Pass |
| 26-oct-2026 | 10 | Day10_script.py — revision CLI utility + weak topics | Pass (redo tonight) |
| 26-oct-2026 | 09 | Day9_script.py — try/except, text + JSON test data | Pass (redo tonight) |
| 26-oct-2026 | 08 | Day8_script.py — functions for login/string/format | Pass (redo tonight) |
| 26-oct-2026 | 07 | Day7_script.py — dicts, sets, unique usernames | Pass (redo tonight) |
| 26-oct-2026 | 06 | Day6_script.py — lists, slices, tuples, status counts | Pass |
| 26-oct-2026 | 05 | Day5_script.py — for/while, counts, paired test lists | Pass |
| 26-oct-2026 | 04 | Day4_script.py — if/elif/else, login tree, password checks | Pass |
| 26-oct-2026 | 03 | Day3_script.py — arithmetic, comparisons, logic, pass/fail rules | Pass |
| 26-oct-2026 | 02 | Day2_script.py — types, conversion, f-strings, summary printer | Pass |
| 26-oct-2026 | 01 | first_python_program.py — name, role, goal, date | Pass |

---

When you finish a day: mark concepts `[x]`, set **Status**, add a row to the progress log, then ask for the next day’s assignments (or a review of your code).
