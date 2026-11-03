# Sauce Demo — Day 05 Scenario List

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

## Notes

- Automate first: **TC-01, TC-02, TC-03, TC-04, TC-06, TC-07** (optional: TC-05 or TC-08).
- Change **Status** from `Manual` to `Automated` as each test is done.
- TC-10 can stay Manual if time is short.





1.What flows did you automate?

answer --- i have automated the three flows basically the happy login flow after that negative flow where wrong username and empty password the negative cases and the navigation flow like adding item to add to cart and navigating to the add cart link and verifying 

What did you leave manual, and why (time, flaky, low risk)?

answer -- The only 3 test cases kept manual because the flow of that test cases is already tested and i have some less time 

Why does each automated test matter (what bug would it catch)?

answer --- the every automated test case is important because it can find multiple bugs like 1(the add to cart link is not opening),2(add to cart button is not enable),3(after clicking the add to cart button that product is not visble in the add to cart link),4(after entering wrong username it showing wrong error message or not showing error message just stuck there). Like this multiple bugs we can find out using these automated test cases 