
import os
import pytest
from dotenv import load_dotenv

load_dotenv()


class FormPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.text_input = page.locator("#my-text-id")
        self.password_input = page.get_by_label("Password")
        self.textarea = page.get_by_text("Textarea")
        self.submit_button = page.get_by_role("button", name="Submit")

    # Open form page
    def open(self):
        form_url = os.getenv("FORM_URL")

        if not form_url:
            pytest.fail("FORM_URL is missing")

        self.page.goto(form_url)

    # Enter text
    def enter_text(self, text):
        self.text_input.fill(text)

    # Enter password
    def enter_password(self, password):
        self.password_input.fill(password)

    # Enter message
    def enter_message(self, message):
        self.textarea.fill(message)

    # Submit form
    def submit(self):
        self.submit_button.click()
