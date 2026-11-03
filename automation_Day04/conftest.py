"""1. What belongs in a Page Object?

   Locators and actions that we need to perform on a particular web page belong in the Page Object. For example, entering text, clicking buttons, and filling forms.

2. What belongs in a Test?

   The test scenario and assertions belong in the test file. Assertions are used to compare the actual result with the expected result and verify whether the test has passed or failed."""



import os
import pytest

from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()


@pytest.fixture
def login_page(page: Page):

    base_url = os.getenv("BASE_URL")

    if not base_url:
        pytest.fail("BASE_URL is missing")

    page.goto(base_url + "/web/index.php/auth/login")

    yield page

    page.context.clear_cookies()

