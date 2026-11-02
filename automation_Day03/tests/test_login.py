
import pytest
import json
import os
from playwright.sync_api import Page, expect


with open("test_data/users.json", "r") as file:
    users = json.load(file)


@pytest.mark.parametrize(
    "username, password, expected",
    [
        (user["username"], user["password"], user["expected"])
        for user in users
    ]
)
def test_login(login_page: Page, username, password, expected):

    username_field = login_page.get_by_placeholder("Username")
    username_field.fill(username)

    password_field = login_page.get_by_placeholder("Password")
    password_field.fill(password)

    login_page.get_by_role("button", name="Login").click()

    if expected == "success":

        expect(login_page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        )

    elif expected == "Invalid credentials":

        expect(login_page.get_by_text("Invalid credentials")).to_be_visible(timeout=10000)

    elif expected == "required":

        expect(login_page.get_by_text("Required")).to_be_visible(timeout=10000)
