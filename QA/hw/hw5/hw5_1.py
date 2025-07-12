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


def test_text_in_iframe(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/iframes.html')

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'my-iframe')))

    expected_text = 'semper posuere integer et senectus justo curabitur.'
    normalized_expected_text = expected_text.replace('\n', ' ').strip() # убираем лишние пробелы и переносы для точного сравнения

    found_text = False

    p_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'p')))

    for p_element in p_elements:
        actual_text = p_element.text.replace('\n', ' ').strip()

        if normalized_expected_text in actual_text:
            print(f"Текст '{expected_text}' найден в элементе: {p_element.text}")
            found_text = True
            break


    assert found_text, f"Текст '{expected_text}' не найден"

    driver.switch_to.default_content()


