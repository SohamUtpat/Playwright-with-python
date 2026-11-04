# Sauce Demo — Day 07 (independent challenge + demo)

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
| TC-08 | Remove product from cart; cart updates | happy | P2 | Automated (Day 07) |
| TC-09 | Checkout with missing first name shows validation error | negative | P2 | Manual |
| TC-10 | Full checkout happy path to confirmation | happy | P3 | Manual |

## Day 07 notes

| Item | Detail |
|------|--------|
| New flow | TC-08 — add first inventory item, open cart, remove it, assert empty cart + no badge |
| Full suite | `python -m pytest -v` → expect **8** passed |
| Smoke | `python -m pytest -m smoke -v` → valid login + TC-05/06/08 |
| HTML report | `python -m pytest -v --html=reports/report.html --self-contained-html` |

## Demo checklist (5–10 minutes)

- [ ] Project layout (`tests/`, `pages/`, `test_data/`, `conftest.py`, `.env`)
- [ ] Smoke run and HTML report
- [ ] Locator + assertion choices
- [ ] Fixture setup/cleanup (`login_page` + cookie clear)
- [ ] Parametrize + markers (`smoke` / `regression`)
- [ ] POM vs test responsibilities
- [ ] Day 07 TC-08 flow
- [ ] Gaps / next steps (`SELF_REVIEW.md`)
