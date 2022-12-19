import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import math
import time
#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()  
browser.implicitly_wait(5)
try:

    browser.get(link)
    

    button = browser.find_element(By.ID, "verify")
    
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

    
finally:
    input("Press Enter to continue...")
    # закрываем браузер после всех манипуляций
    browser.quit()