import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()  
browser.implicitly_wait(5)
try:

    browser.get(link)
    
    button = browser.find_element(By.ID, "book")
    lol = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    
    button.click()
    #message = browser.find_element(By.ID, "verify_message")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    x_element = browser.find_element(By.CSS_SELECTOR, "input#answer")
    x_element.send_keys(y)
    button = browser.find_element(By.ID,"solve")
    button.click()


    
finally:
    input("Press Enter to continue...")
    # закрываем браузер после всех манипуляций
    browser.quit()