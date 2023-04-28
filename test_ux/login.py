import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:8000")
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='/accounts/login/']").click()
time.sleep(3)
driver.find_element(By.ID, 'id_username').send_keys('admin')
driver.find_element(By.ID, 'id_password').send_keys('12345')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)