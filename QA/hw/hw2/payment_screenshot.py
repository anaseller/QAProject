
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
driver = webdriver.Firefox(service=Service(), options=options)
driver.get('https://itcareerhub.de/ru')
sleep(2)

payment_link = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
payment_link.click()
sleep(3)

driver.save_screenshot('payment_section.png')
sleep(2)

driver.quit()