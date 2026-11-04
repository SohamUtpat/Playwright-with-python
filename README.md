# Python · Pytest · Playwright Automation

UI test automation practice built around a 7-day Playwright plan. The suite uses **Python**, **Pytest**, and **Playwright** with the **Page Object Model**, external test data, env-based URLs, and smoke/regression markers.

**Demo app (Days 5–7):** [Sauce Demo](https://www.saucedemo.com/)

---

## Stack

| Tool | Role |
|------|------|
| Python 3 | Runtime |
| Pytest | Test runner, fixtures, parametrize, markers |
| Playwright + pytest-playwright | Browser automation |
| python-dotenv | Load `BASE_URL` from `.env` |
| pytest-html | HTML test reports |
| Page Object Model | Locators and actions in `pages/`; assertions stay in tests |

---

## Project layout

```
Python, Pytest and Playwright/
├── requirements.txt
├── README.md
├── PLAYWRIGHT_7_DAY_PROGRESS.md
├── automation_Day01/         # Setup, locators, assertions
├── automation_Day02/         # Waits, web-first assertions, debugging
├── automation_Day03/         # Fixtures, parametrize, JSON + .env
├── automation_Day04/         # Page Object Model
├── automation_Day05/         # Sauce Demo mini-project
├── automation_Day06/         # Stability, reporting, multi-browser
└── automation_Day07/         # Independent challenge + demo (current)
    ├── .env                  # BASE_URL (not committed)
    ├── conftest.py           # login_page fixture
    ├── pytest.ini            # smoke / regression markers
    ├── scenarios.md          # TC list + demo checklist
    ├── SELF_REVIEW.md        # Strengths / gaps / next steps
    ├── pages/
    │   ├── login_page.py
    │   ├── inventory_page.py
    │   └── cart_page.py
    ├── test_data/
    │   ├── users.json
    │   └── products.json
    ├── tests/
    │   ├── test_login.py
    │   └── test_inventory.py
    └── reports/              # Generated HTML reports (gitignored)
```

Use **`automation_Day07`** as the main runnable suite.

---

## Setup

From the project root (same Python you use for `python -m pytest` — no virtualenv required for this learning project):

### 1. Install dependencies

```powershell
python -m pip install -r requirements.txt
python -m playwright install
```

Install only the browsers you need if you prefer:

```powershell
python -m playwright install chromium
# optional: python -m playwright install firefox webkit
```

### 2. Configure `.env`

Create `automation_Day07/.env` (or copy from an earlier day folder):

```env
BASE_URL=https://www.saucedemo.com/
```

`conftest.py` fails the run if `BASE_URL` is missing.

---

## How the suite is organized

### Fixtures (`conftest.py`)

- `login_page` — opens `BASE_URL`, yields the Playwright `page`, then clears cookies so tests stay independent (no leftover session/cart).

### Page objects (`pages/`)

- **LoginPage** — username, password, login button, error message; `login(username, password)`.
- **InventoryPage** — product list, cart badge/link; `add_to_cart(name)`, `open_cart()`.

### Test data (`test_data/`)

- `users.json` — login rows (`username`, `password`, `expected`, `mark`).
- `products.json` — product names used for add-to-cart checks.

### Markers (`pytest.ini`)

| Marker | Meaning |
|--------|---------|
| `smoke` | Quick checks for main paths (valid login, inventory list, cart badge) |
| `regression` | Extra validation (wrong password, empty username, locked-out user, cart contents) |

---

## Automated coverage (Day 07)

| ID | Scenario | Marker |
|----|----------|--------|
| TC-01 | Valid login → inventory | smoke |
| TC-02 | Wrong password → error | regression |
| TC-03 | Empty username → error | regression |
| TC-04 | Locked-out user → error | regression |
| TC-05 | Inventory list visible after login | smoke |
| TC-06 | Add product → cart badge `1` | smoke |
| TC-07 | Open cart → product name visible | regression |
| TC-08 | Remove from cart → empty cart (Day 07) | smoke |

Manual backlog (TC-09–10): checkout validation, full checkout — see `automation_Day07/scenarios.md`.

---

## Run commands

Always run from the day folder so `pytest.ini`, `.env`, and relative `test_data/` paths resolve:

```powershell
cd "automation_Day07"
```

### Full suite

```powershell
python -m pytest -v
```

### Smoke only (Chromium)

```powershell
python -m pytest -m smoke --browser chromium -v
```

### Regression only

```powershell
python -m pytest -m regression -v
```

### Other browsers

```powershell
python -m pytest -m smoke --browser firefox -v
python -m pytest -m smoke --browser webkit -v
```

### Headed / slow motion (debugging)

```powershell
python -m pytest -v --headed
python -m pytest -v --headed --slowmo 500
```

### Single file or test

```powershell
python -m pytest tests/test_login.py -v
python -m pytest tests/test_inventory.py::test_add_product_shows_cart_badge -v
```

### HTML report

```powershell
mkdir reports -ErrorAction SilentlyContinue
python -m pytest -v --html=reports/report.html --self-contained-html
start reports\report.html
```

### HTML report + screenshot on failure

```powershell
python -m pytest -v --html=reports/fail_report.html --self-contained-html --screenshot=only-on-failure
```

Screenshots land under `test-results/` (for example `test-results/.../test-failed-1.png`).

---

## Design notes

- **Page object vs test:** locators and user actions live in page classes; expected outcomes are asserted in the test.
- **No hard-coded sleeps:** rely on Playwright auto-waiting and web-first `expect(...)` assertions.
- **Independence:** each test starts from a fresh login page context; fixture teardown clears cookies.
- **Config outside tests:** URLs in `.env`; credentials and products in JSON.
- **Generated artifacts:** `reports/` and `test-results/` are created by runs; they are not source files.

---

## Progress

Track day-by-day status in [`PLAYWRIGHT_7_DAY_PROGRESS.md`](PLAYWRIGHT_7_DAY_PROGRESS.md).
