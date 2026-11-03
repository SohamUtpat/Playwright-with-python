import pytest
import json

from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


with open("test_data/users.json", "r") as file:
    users = json.load(file)


def _mark_for(user):
    name = user.get("mark", "regression")
    return getattr(pytest.mark, name)


@pytest.mark.parametrize(
    "username, password, expected",
    [
        pytest.param(
            user["username"],
            user["password"],
            user["expected"],
            marks=_mark_for(user),
            id=f"{user['username'] or 'empty'}-{user['expected']}",
        )
        for user in users
    ],
)
def test_login(login_page, username, password, expected):

    login = LoginPage(login_page)

    login.login(username, password)

    # TC-01 — valid login lands on inventory
    if expected == "success":

        inventory = InventoryPage(login_page)
        expect(inventory.inventory_list).to_be_visible()

    # TC-02 — wrong password
    elif expected == "Invalid":

        expect(login.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service"
        )

    # TC-03 — empty username
    elif expected == "username_required":

        expect(login.error_message).to_have_text(
            "Epic sadface: Username is required"
        )

    # TC-04 — locked-out user
    elif expected == "locked":

        expect(login.error_message).to_have_text(
            "Epic sadface: Sorry, this user has been locked out."
        )
