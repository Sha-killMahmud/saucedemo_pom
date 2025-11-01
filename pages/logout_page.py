import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logout:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)

