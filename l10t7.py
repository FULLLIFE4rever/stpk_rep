import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import math
import time
#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/wait2.html"
browser = webdriver.Chrome()  
browser.implicitly_wait(5)
try:

    browser.get(link)
    

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

    
finally:
    input("Press Enter to continue...")
    # закрываем браузер после всех манипуляций
    browser.quit()