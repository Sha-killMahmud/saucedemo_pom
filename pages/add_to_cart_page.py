import time
from selenium.webdriver.common.by import By

class AddToCart:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                product.find_element(By.TAG_NAME, "button").click()
                break
        time.sleep(1)