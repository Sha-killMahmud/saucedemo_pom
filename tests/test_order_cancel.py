import time
import pytest
import os
from selenium.webdriver.common.by import By
from pages.add_to_cart_page import AddToCart
from pages.go_to_cart_page import GoToCart
from pages.checkout_page import Checkout
from pages.logout_page import Logout


@pytest.mark.skipif(os.getenv("SKIP_CANCEL") == "1", reason="Cancel test skipped by environment flag")
@pytest.mark.order(3)
def test_order_cancel(setup_driver):
    driver = setup_driver
    addToCart = AddToCart(driver)
    addToCart.add_to_cart("Sauce Labs Bike Light")
    goToCart = GoToCart(driver)
    goToCart.go_to_cart()
    checkout = Checkout(driver)
    checkout.checkout("Shakil", "Mahmud", "1205")
    driver.find_element(By.ID, "cancel").click()
    homepage = "https://www.saucedemo.com/inventory.html"
    assert homepage in driver.current_url
    time.sleep(2)
    logout = Logout(driver)
    logout.logout()