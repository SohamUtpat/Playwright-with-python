class InventoryPage:

    def __init__(self, page):
        self.page = page

        # locators
        self.inventory_list = page.locator(".inventory_list")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_to_cart(self, product_name):
        # scope to the product card, then click its Add to cart button
        item = self.page.locator(".inventory_item").filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        self.cart_link.click()
