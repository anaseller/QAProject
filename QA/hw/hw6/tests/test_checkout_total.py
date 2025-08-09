from QA.hw.hw6.tests.base_test import BaseTest

class TestCheckoutTotal(BaseTest):
    def test_checkout_total(self):
        #Откройте сайт магазина
        self.login_page.open()

        # Авторизуйтесь как пользователь standard_user.
        self.login_page.success_login('standard_user', 'secret_sauce')
        assert 'inventory.html' in self.driver.current_url, 'Не удалось войти в систему'

        # Добавьте в корзину товары:
        self.inventory_page.add_item_to_cart('Sauce Labs Backpack')
        self.inventory_page.add_item_to_cart('Sauce Labs Bolt T-Shirt')
        self.inventory_page.add_item_to_cart('Sauce Labs Onesie')

        # Перейдите в корзину.
        self.inventory_page.go_to_cart()

        # Нажмите Checkout.
        self.cart_page.proceed_to_checkout()

        # Заполните форму своими данными
        self.checkout_page.fill_checkout_info('Test', 'User', '12345')
        self.checkout_page.continue_checkout()

        # Прочтите со страницы итоговую стоимость (Total).
        total = self.checkout_page.get_total_price()

        # Проверьте, что итоговая сумма равна 'Total: $58.29'.
        assert total == 'Total: $58.29', f'Ожидалось Total: $58.29, но получено {total}'