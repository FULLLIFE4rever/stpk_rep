from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    x_element = browser.find_element(By.CSS_SELECTOR, "input#answer")
    x_element.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    button = browser.find_element(By.TAG_NAME,"button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    input("Press Enter to continue...")
    # закрываем браузер после всех манипуляций
    browser.quit()