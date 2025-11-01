import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoToCart:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        cart_icon = (By.ID, "shopping_cart_container")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(cart_icon)).click()
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(1)