from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checkout_button = (By.ID, 'checkout')

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()
        self.wait.until(EC.url_contains('checkout-step-one.html'))