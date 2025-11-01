import time
from selenium.webdriver.common.by import By
from pages.go_to_cart_page import GoToCart


class GetCartItems:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        # goToCart = GoToCart(self)
        # goToCart.go_to_cart()
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        result = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            qty = item.find_element(By.CLASS_NAME, "cart_quantity").text
            desc = item.find_element(By.CLASS_NAME, "inventory_item_desc").text
            result.append({'name' :name, 'price' :price, 'qty' : qty, 'desc' : desc})
        time.sleep(1)
        return result