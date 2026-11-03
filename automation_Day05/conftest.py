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

    page.goto(base_url)

    yield page

    page.context.clear_cookies()
