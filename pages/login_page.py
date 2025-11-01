import time
from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, driver, username, password):
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
