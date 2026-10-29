#Assignment A: Happy Path (valid flow)

from playwright.sync_api import Page, expect

def test_happy_path(page: Page):

    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    text_input = page.locator("#my-text-id")
    text_input.fill("Soham Utpat")
    expect(text_input).to_have_value("Soham Utpat")

    password = page.get_by_label("Password")
    password.fill("Test@123")
    expect(password).to_have_value("Test@123")

    text_area = page.locator('[name="my-textarea"]')
    text_area.fill("Learning the automation testing using Playwright tool")
    expect(text_area).to_have_value("Learning the automation testing using Playwright tool")

    
    page.get_by_role("button", name = "Submit").click()
    
    message = page.locator("#message")
    expect(message).to_have_text("Received!")
    
    submission_text = page.locator(".display-6")
    expect(submission_text).to_have_text("Form submitted")


#Assignment B: Invalid Case1 (wrong username)

def test_invalid_case1(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username = page.locator('[name = "username"]')
    username.fill("admin1")
    expect(username).to_have_value("admin1")

    password = page.get_by_placeholder("Password")
    password.fill("admin123")
    expect(password).to_have_value("admin123")

    expect(page.get_by_text("Forgot your password?")).to_be_visible()

    page.get_by_role("button", name = "Login").click()

    expect(page.get_by_text("Invalid credentials")).to_be_visible(timeout = 10000)


#Assignment C: Invalid Case2 (empty password)

def test_empty_password(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username = page.get_by_placeholder("Username")
    username.fill("Admin")
    expect(username).to_have_value("Admin")

    expect(page.get_by_placeholder("Password")).to_be_visible()

    expect(page.get_by_role("button", name ="Login")).to_be_visible()

    page.get_by_role("button", name ="Login").click()

    expect(page.get_by_text("required")).to_be_visible()

#Assignment D: Web first assertions 

def test_web_first_assertion(page: Page):

    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    expect(page).to_have_title("Web form")
    expect(page.get_by_text("Web form")).to_be_visible()

    text_insert = page.locator("#my-text-id")
    text_insert.fill("Soham")
    expect(text_insert).to_have_value("Soham")

    password = page.get_by_label("Password")
    password.fill("test123")
    expect(password).to_have_value("test123")

    checkbox = page.locator("#my-check-1")
    expect(checkbox).to_be_checked()

    expect(page.get_by_role("button", name ="Submit")).to_be_enabled()
    page.get_by_role("button", name ="Submit").click()

    message = page.locator("#message")
    expect(message).to_have_text("Received!")

    text = page.locator(".display-6")
    expect(text).to_contain_text("Form submitted")





