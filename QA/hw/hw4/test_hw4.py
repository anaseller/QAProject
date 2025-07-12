from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_button_text_change(driver):
    driver.get("http://uitestingplayground.com/textinput")
    wait = WebDriverWait(driver, 10)

    # Вводим текст
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")

    # Нажимаем синюю кнопку
    button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    button.click()

    # Проверяем, что текст кнопки изменился
    updated_button = driver.find_element(By.ID, "updatingButton")
    assert updated_button.text == "ITCH", f"Ожидался текст 'ITCH', но получен: {updated_button.text}"


def test_image_loading_and_alt(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 20)

    # Ждем, пока на странице появится минимум 4 видимых изображения - иначе тест принимает 2 картинку за 3 и выдает ошибку
    images = wait.until(lambda d: [img for img in d.find_elements(By.TAG_NAME, 'img')
        if img.is_displayed() and img.get_attribute('alt') != ''] if len(
        [img for img in d.find_elements(By.TAG_NAME, 'img') if
         img.is_displayed() and img.get_attribute('alt') != '']) >= 4 else False)

    # Проверяем третье изображение
    third_img_alt = images[2].get_attribute('alt')
    assert third_img_alt == 'award', f"Ожидался alt 'award', но получен: '{third_img_alt}'"