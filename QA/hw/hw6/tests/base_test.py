import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from QA.hw.hw6.pages.login_page import LoginPage
from QA.hw.hw6.pages.inventory_page import InventoryPage
from QA.hw.hw6.pages.cart_page import CartPage
from QA.hw.hw6.pages.checkout_page import CheckoutPage

class BaseTest:
    @pytest.fixture(scope='class', autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()

        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.inventory_page = InventoryPage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.checkout_page = CheckoutPage(driver)

        yield
        driver.quit()