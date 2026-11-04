import json

import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


with open("test_data/users.json", "r") as file:
    users = json.load(file)

with open("test_data/products.json", "r") as file:
    products = json.load(file)

# reuse the valid login row; load product name once for add + assert
VALID_USER = next(user for user in users if user["expected"] == "success")
PRODUCT = products[0]


@pytest.mark.smoke
def test_inventory_list_visible_after_login(login_page):
    # TC-05
    login = LoginPage(login_page)
    login.login(VALID_USER["username"], VALID_USER["password"])

    inventory = InventoryPage(login_page)
    expect(inventory.inventory_list).to_be_visible()


@pytest.mark.smoke
def test_add_product_shows_cart_badge(login_page):
    # TC-06
    login = LoginPage(login_page)
    login.login(VALID_USER["username"], VALID_USER["password"])

    inventory = InventoryPage(login_page)
    inventory.add_to_cart(PRODUCT["name"])

    expect(inventory.cart_badge).to_have_text("1")


@pytest.mark.regression
def test_added_product_visible_in_cart(login_page):
    # TC-07
    login = LoginPage(login_page)
    login.login(VALID_USER["username"], VALID_USER["password"])

    inventory = InventoryPage(login_page)
    inventory.add_to_cart(PRODUCT["name"])
    inventory.open_cart()

    cart = CartPage(login_page)
    expect(cart.item_named(PRODUCT["name"])).to_be_visible()


@pytest.mark.smoke
def test_login_add_first_item_then_remove_from_cart(login_page):
    # TC-08 — login → add first item → open cart → remove item → cart is empty
    login = LoginPage(login_page)
    login.login(VALID_USER["username"], VALID_USER["password"])

    inventory = InventoryPage(login_page)
    expect(inventory.inventory_list).to_be_visible()

    first_item_name = inventory.first_item_name()
    inventory.add_first_item_to_cart()
    expect(inventory.cart_badge).to_have_text("1")

    inventory.open_cart()

    cart = CartPage(login_page)
    expect(cart.item_named(first_item_name)).to_be_visible()
    cart.remove_item(first_item_name)

    expect(cart.cart_items).to_have_count(0)
    expect(cart.cart_badge).to_have_count(0)
