class CartPage:

    def __init__(self, page):
        self.page = page

        # locators
        self.cart_list = page.locator(".cart_list")
        self.cart_items = page.locator(".cart_item")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def item_named(self, product_name):
        return self.page.get_by_text(product_name)

    def remove_item(self, product_name):
        item = self.cart_items.filter(has_text=product_name)
        item.get_by_role("button", name="Remove").click()
