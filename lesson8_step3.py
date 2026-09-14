import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link  = "https://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    result = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    # browser.find_element(By.TAG_NAME, "select").click()
    # browser.find_element(By.CSS_SELECTOR, f"[value='{result}']").click()

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(3)
    browser.quit()