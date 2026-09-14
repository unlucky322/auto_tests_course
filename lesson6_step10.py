import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "https://suninjuly.github.io/registration1.html" # successfully 
link2 = "https://suninjuly.github.io/registration2.html" # unsuccessfully

try:

    browser = webdriver.Chrome()
    browser.get(link1) # change to link2 to test the second page


    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Name")

    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Lastname")

    input3 = browser.find_element(By.CSS_SELECTOR, 'input.third')
    input3.send_keys("Email")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()
