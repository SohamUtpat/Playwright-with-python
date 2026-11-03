# Sauce Demo — Day 06 (stability + reporting)

**App:** https://www.saucedemo.com/  
**Users:** `standard_user`, `locked_out_user`, etc.  
**Password (all users):** `secret_sauce`

| ID | Title | Type | Priority | Status |
|----|--------|------|----------|--------|
| TC-01 | Valid login (`standard_user`) lands on inventory | happy | P1 | Automated |
| TC-02 | Wrong password shows error message | negative | P1 | Automated |
| TC-03 | Empty username and/or password shows error | negative | P1 | Automated |
| TC-04 | Locked-out user (`locked_out_user`) cannot log in | negative | P1 | Automated |
| TC-05 | Inventory page shows product list after login | navigation | P1 | Automated |
| TC-06 | Add one product; cart badge shows `1` | happy | P1 | Automated |
| TC-07 | Open cart; added product name is visible | navigation | P2 | Automated |
| TC-08 | Remove product from cart; cart updates | happy | P2 | Manual |
| TC-09 | Checkout with missing first name shows validation error | negative | P2 | Manual |
| TC-10 | Full checkout happy path to confirmation | happy | P3 | Manual |

## Day 06 notes (fill in as you work)

| Run | Command | Result | Notes |
|-----|---------|--------|-------|
| 1 | `python -m pytest -v` | 7 passed (6.75s) | 1 pytest-playwright deprecation warning (base_url) — not a flake |
| 2 | `python -m pytest -v` | 7 passed (4.80s) | same warning; still green |
| 3 | `python -m pytest -v` | 7 passed (4.53s) | same warning; still green |
| Smoke | `python -m pytest -m smoke --browser chromium` | 3 passed, 4 deselected (2.51s) | inventory list, cart badge, valid login |
| Other browser (optional) | `--browser firefox` / `--browser webkit` | 3 passed each (37.7s / 27.6s) | smoke green on all three engines |

**Independence check:** Pass — single inventory test alone (1 passed); `test_login.py` alone (4 passed); full `tests/` suite (7 passed). Cookie clear in `login_page` fixture keeps session/cart from leaking between tests.  
**Failure evidence path:** `test-results/.../test-failed-1.png` (locked_out_user; deliberate wrong expected text)  
**HTML report path:** `reports/report.html`, `reports/fail_report.html`  
