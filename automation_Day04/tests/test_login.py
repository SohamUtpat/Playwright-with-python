import pytest
import json

from playwright.sync_api import expect
from pages.login_page import LoginPage


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

    if expected == "success":

        expect(login_page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        )

    elif expected == "Invalid credentials":

        expect(login.error_message).to_be_visible(timeout=10000)

    elif expected == "required":

        expect(login_page.get_by_text("Required")).to_be_visible(timeout=10000)
