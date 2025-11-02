import time
from pages.add_to_cart_page import AddToCart
from pages.get_cart_items_page import GetCartItems
from pages.go_to_cart_page import GoToCart
from pages.checkout_page import Checkout
from pages.logout_page import Logout


@pytest.mark.dependency(name="checkout_verification")
@pytest.mark.order(1)
def test_checkout_details_verification(setup_driver, retry_on_failure):
    with retry_on_failure:  # Wrap the test in retry logic
        driver = setup_driver
        addToCart = AddToCart(driver)
        products_to_add = ['Sauce Labs Bike Light' , 'Sauce Labs Bolt T-Shirt']

        for product in products_to_add:
            addToCart.add_to_cart(product)
        goToCart = GoToCart(driver)
        goToCart.go_to_cart()
        checkout = Checkout(driver)
        checkout.checkout("Shakil", "Mahmud", "1205")
        getCartItems = GetCartItems(driver)
        items = getCartItems.get_cart_items()
        actual_names = [item['name'] for item in items]

        for expected in products_to_add:
            assert expected in actual_names, f'Expected {expected} in cart but not found!'
        time.sleep(2)
        logout = Logout(driver)
        logout.logout()