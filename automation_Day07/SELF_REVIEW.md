# Day 07 — Self-review

## Strengths (what went well)

- Built TC-08 independently: add first item → cart → remove → empty cart assertions.
- Kept POM clear with a dedicated `CartPage` for cart actions.
- Reused Day 3–6 patterns: fixture + `.env`, JSON users/products, smoke/regression markers.

## Needs more practice

- Explaining failures from report/screenshot without re-running blindly.
- Choosing when a new page object is worth it vs extending an existing one.
- Comfortable Trace Viewer / Inspector walkthrough in a live demo.

## Trade-offs I can explain

- TC-08 reads the first product name from the UI (flexible) vs hard-coding from `products.json` (stable named product for TC-06/07).
- Manual TC-09/10 left for later — checkout is valuable but longer; week goal was one new independent flow.
- Assertions stay in tests; pages only expose locators and user actions.

## Next learning steps (after this week)

- Basic CI command to run smoke on every push.
- Optional safe demo API check alongside UI.
- Deeper Trace Viewer practice on a deliberate failure.

## Demo notes

- Show TC-08 as the Day 07 addition; show one negative login row for parametrize.
- Mention cookie clear keeps cart state from leaking between tests.
