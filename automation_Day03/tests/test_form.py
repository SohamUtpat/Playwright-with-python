import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

@pytest.mark.smoke
def test_form_submits_shows_received_message(page: Page):

    form_url = os.getenv("FORM_URL")

    if not form_url:
        pytest.fail("FORM_URL is missing")

    page.goto(form_url)

    text_input = page.locator("#my-text-id")
    text_input.fill("Om ingle")
    expect(text_input).to_have_value("Om ingle")

    password_input = page.get_by_label("Password")
    password_input.fill("admin123")
    expect(password_input).to_have_value("admin123")

    info = page.get_by_text("Textarea")
    info.fill("Learned the basic foundation of automation testing")
    expect(info).to_have_value("Learned the basic foundation of automation testing")

    page.get_by_role("button", name = "Submit").click()

    expect(page.locator(".lead")).to_have_text("Received!")

    expect(page.get_by_text("Form submitted")).to_have_text("Form submitted")
