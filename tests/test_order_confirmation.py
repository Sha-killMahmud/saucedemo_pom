import time
import pytest
from selenium.webdriver.common.by import By
from pages.add_to_cart_page import AddToCart
from pages.go_to_cart_page import GoToCart
from pages.checkout_page import Checkout
from pages.logout_page import Logout


@pytest.mark.dependency(depends=["checkout_verification"])
@pytest.mark.order(2)
@pytest.mark.flaky(reruns=2)
def test_order_confirmation(setup_driver):
    driver = setup_driver
    addToCart = AddToCart(driver)
    addToCart.add_to_cart("Sauce Labs Bike Light")
    goToCart = GoToCart(driver)
    goToCart.go_to_cart()
    checkout = Checkout(driver)
    checkout.checkout("Shakil", "Mahmud", "1205")
    driver.find_element(By.ID, "finish").click()
    confirmation_text = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you" in confirmation_text
    time.sleep(2)
    logout = Logout(driver)
    logout.logout()
