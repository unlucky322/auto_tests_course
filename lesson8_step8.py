import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "test_lesson8.txt")
link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Name")
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']").send_keys("LastName")
    browser.find_element(By.XPATH, "//input[@name='email']").send_keys("email@example.com")
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(3)
    browser.quit()