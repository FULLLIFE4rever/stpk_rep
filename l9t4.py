import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
link = " http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:

    browser.get(link)
    

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    x_element = browser.find_element(By.CSS_SELECTOR, "input#answer")
    x_element.send_keys(y)
    button = browser.find_element(By.TAG_NAME,"button")
    button.click()
finally:
    input("Press Enter to continue...")
    # закрываем браузер после всех манипуляций
    browser.quit()