class InventoryPage:

    def __init__(self, page):
        self.page = page

        # locators
        self.inventory_list = page.locator(".inventory_list")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_to_cart(self, product_name):
        # scope to the product card, then click its Add to cart button
        item = self.inventory_items.filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def add_first_item_to_cart(self):
        # first product card on the inventory page
        self.inventory_items.first.get_by_role("button", name="Add to cart").click()

    def first_item_name(self):
        return self.inventory_items.first.locator(".inventory_item_name").inner_text()

    def open_cart(self):
        self.cart_link.click()
