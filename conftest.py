import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login


@pytest.fixture(scope="function")
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    login = Login(driver)
    login.login(driver, "standard_user", "secret_sauce")
    assert 'inventory' in driver.current_url
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def retry_on_failure():
    for attempt in range(3):  # Maximum 3 attempts
        try:
            yield
            break  # If test passes, break out of the loop
        except Exception as e:
            if attempt == 2:  # Last attempt
                raise  # Re-raise the exception if all attempts failed
            continue


@pytest.fixture(scope="session")
def test_products():
    return [
        ['Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt'],
        ['Sauce Labs Bike Light'],
        ['Sauce Labs Bolt T-Shirt']
    ]