
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_field = (By.ID, 'first-name')
        self.last_name_field = (By.ID, 'last-name')
        self.postal_code_field = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.finish_button = (By.ID, 'finish')
        self.total_sum = (By.CSS_SELECTOR, '.summary_total_label')

    def fill_checkout_info(self, first_name, last_name, postal_code):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.first_name_field)).send_keys(first_name)
        self.wait.until(EC.element_to_be_clickable(self.last_name_field)).send_keys(last_name)
        self.wait.until(EC.element_to_be_clickable(self.postal_code_field)).send_keys(postal_code)

    def continue_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def get_total_price(self):
        total_element = self.wait.until(EC.visibility_of_element_located(self.total_sum))
        return total_element.text

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_button)).click()