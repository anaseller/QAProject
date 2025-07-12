# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# 
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
# 
# def test_elements(driver):
#     driver.get("https://itcareerhub.de/ru")
# 
#     wait = WebDriverWait(driver, 10)
# 
#     # Проверка логотипа
#     logo = driver.find_element(By.XPATH, '//img[contains(@src, "Group_3793.svg")]')
#     assert logo.is_displayed(), "Логотип не отображается"
# 
#     # Проверка ссылок
#     menu_texts = [
#         "Программы",
#         "Способы оплаты",
#         "Новости",
#         "О нас",
#         "Отзывы"
#     ]
# 
#     for text in menu_texts:
#         try:
#             link = driver.find_element(By.XPATH, f'//a[text()="{text}"]')
#             assert link.is_displayed(), f'Ссылка "{text}" не отображается'
#         except NoSuchElementException:
#             assert False, f'Ссылка "{text}" не найдена на странице'
# 
#     # Проверка кнопок переключения языка
#     lang_ru = driver.find_element(By.XPATH, '//a[contains(text(), "ru")]')
#     lang_de = driver.find_element(By.XPATH, '//a[contains(text(), "de")]')
#     assert lang_ru.is_displayed(), 'Кнопка RU не отображается'
#     assert lang_de.is_displayed(), 'Кнопка DE не отображается'
# 
#     # Кликнуть по иконке с телефонной трубкой
#     phone_icon = driver.find_element(By.XPATH, '//img[contains(@src, "Group_3800.svg")]')
#     phone_icon.click()
# 
#     # Проверка текста после клика
#     text_locator = '//div[contains(text(), "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами")]'
#     popup_text = wait.until(EC.visibility_of_element_located((By.XPATH, text_locator)))
#     assert popup_text.is_displayed(), "Текст после клика по трубке не отображается"