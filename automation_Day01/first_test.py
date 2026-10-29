#Assignment A: 
from playwright.sync_api import Page, expect

def test_web_form_title(page: Page):
    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    expect(page).to_have_title("Web form")

#Assignment B:

def test_first_real_test(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    expect(page).to_have_title("Demo Web Shop")

    expect(page.get_by_role("heading", name = "Welcome to our store")).to_be_visible()

#Assignment C: Locator drill

def test_locator_drill(page: Page):
    page.goto("https://sauce-demo.myshopify.com/")

    expect(page.get_by_role("link", name = "Check Out")).to_be_visible()

    expect(page.get_by_text("Just a demo site showing off what Sauce can do.")).to_be_visible()

    expect(page.get_by_placeholder("Search")).to_be_visible()

    page.goto("https://sauce-demo.myshopify.com/account/login")

    expect(page.get_by_label("Email Address")).to_be_visible()


#Assignment D: Form fields 

def test_form_fields(page: Page):

    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    text_field = page.locator('[name="my-text"]')
    text_field.fill("Hello Playwright")   

    expect(text_field).to_have_value("Hello Playwright")

    page.get_by_role("button", name="Submit").click()

    message = page.locator("#message")
    expect(message).to_have_text("Received!") 

#Assignment E: Intentionally break locator

def test_break_locator(page: Page):

    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    page.get_by_role("button", name="Submit123").click()



    