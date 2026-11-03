
import pytest

from playwright.sync_api import expect
from pages.form_page import FormPage


@pytest.mark.smoke
def test_form_submits_shows_received_message(page):

    form = FormPage(page)

    form.open()

    form.enter_text("Soham Utpat")
    form.enter_password("admin123")
    form.enter_message("Learned the basic foundation of automation testing")

    form.submit()

    expect(page.locator(".lead")).to_have_text("Received!")

    expect(page.get_by_text("Form submitted")).to_have_text("Form submitted")
