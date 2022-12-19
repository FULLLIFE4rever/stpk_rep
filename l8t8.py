import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:

    browser.get(link)
    
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR,"[placeholder='Enter first name']")
    element.send_keys("First name")
    element = browser.find_element(By.CSS_SELECTOR,"[placeholder='Enter last name']")
    element.send_keys("First name")
    element = browser.find_element(By.CSS_SELECTOR,"[placeholder='Enter email']")
    element.send_keys("First@name.org")
    element = browser.find_element(By.CSS_SELECTOR,"#file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    input("Press Enter to continue...")
    # закрываем браузер после всех манипуляций
    browser.quit()