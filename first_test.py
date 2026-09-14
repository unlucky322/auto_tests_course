import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(2)

driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(2)

textarea = driver.find_element(By.CLASS_NAME, "textarea")

textarea.send_keys("something")

time.sleep(2)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

submit_button.click()
time.sleep(2)

driver.quit()