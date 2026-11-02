"""import pytest

from playwright.sync_api import expect

@pytest.fixture

def login_page(page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("button", name ="Login")).to_be_visible()

    yield page

    page.context.clear_cookies()

    print("Teardown completed: Browser cookies cleared")"""

    
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

    return page
