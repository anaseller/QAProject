
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_drag_and_drop(driver):
    driver.get('https://www.globalsqa.com/demo-site/draganddrop/')

    #кликаем на куки-капчу
    consent_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Соглашаюсь']")))
    consent_button.click()
    print("Успешно кликнули по кнопке 'Соглашаюсь'")

    #кликаем по вкладке Photo Manager
    photo_manager_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'Photo Manager'))
    )
    photo_manager_tab.click()
    print("Успешно кликнули по вкладке 'Photo Manager'")

    #переключаемся на iframe
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[data-src*='photo-manager.html']"))
    )
    print("Успешно переключились на iframe")

    #находим изображение и корзину
    source_image = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#gallery li:first-child img"))
    )
    source_image_alt = source_image.get_attribute('alt')
    print(f"Найдено исходное изображение: {source_image_alt}")

    trash_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'trash'))
    )

    #выполняем Drag & Drop
    actions = ActionChains(driver)
    actions.click_and_hold(source_image).move_to_element(trash_element).release().perform()
    print("Изображение успешно перетащено в корзину")

    #проверяем, что в корзине появилась одна фотография
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"#trash ul li img[alt='{source_image_alt}']"))
    )
    print(f"Обнаружено изображение '{source_image_alt}' в корзине")

    items_in_trash = driver.find_elements(By.CSS_SELECTOR, "#trash ul li")
    assert len(items_in_trash) == 1, f'Ожидался 1 элемент в корзине, но найдено {len(items_in_trash)}'
    print(f'В корзине {len(items_in_trash)} фотография(й) (ожидалась 1)')

    #проверяем, что в галерее осталось 3 фотографии
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, f"#gallery li img[alt='{source_image_alt}']"))
    )

    items_in_gallery = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
    assert len(items_in_gallery) == 3, f'Ожидалось 3 фотографии в галерее, но найдено {len(items_in_gallery)}'
    print(f'В галерее осталось {len(items_in_gallery)} фотографии (ожидалось 3)')

    driver.switch_to.default_content()






# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_drag_and_drop_image_to_trash(driver):
#     driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
#
#     #сначала кликаем на куки-капчу, иначе дальше тест упадет
#     consent_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Соглашаюсь']")))
#     consent_button.click()
#
#     photo_manager_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Photo Manager')))
#     photo_manager_tab.click()
#
#     WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@data-src, 'photo-manager.html')]")))
#
#
#     source_image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//ul[@id='gallery']/li[1]/img")))
#     source_image_alt = source_image.get_attribute('alt')
#
#     trash_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'trash')))
#
#     actions = ActionChains(driver)
#     actions.click_and_hold(source_image).move_to_element(trash_element).release().perform()
#     print('Изображение перетащено в корзину')
#
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//div[@id='trash']/ul/li/img[@alt='{source_image_alt}']")))
#     print(f"Изображение '{source_image_alt}' в корзине")
#
#     items_in_trash = driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li")
#     assert len(items_in_trash) == 1, f'Ожидался 1 элемент в корзине, но найдено {len(items_in_trash)}'
#     print(f'В корзине {len(items_in_trash)} фотография(ии) (ожидался 1)')
#
#
#     WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, f"//ul[@id='gallery']/li/img[@alt='{source_image_alt}']")))
#     items_in_gallery = driver.find_elements(By.XPATH, "//ul[@id='gallery']/li")
#     assert len(items_in_gallery) == 3, f'Ожидалось 3 фотографии в галерее, но найдено {len(items_in_gallery)}'
#     print(f'В галерее осталось {len(items_in_gallery)} фотографии (ожидалось 3)')
#
#
#     driver.switch_to.default_content()