import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationintesting.online/")

driver.find_element(By.XPATH,"//button").click()

time.sleep(2)

driver.find_element(By.XPATH,'//button[@class="btn btn-outline-primary float-right openBooking"]').click()

time.sleep(2)

driver.find_element(By.XPATH,'//*[@name="firstname"]').send_keys("Jhon")
time.sleep(2)

driver.find_element(By.XPATH,'//div[@class="row hotel-room-info"]//div/input[@name="lastname"]').send_keys("Doe")
time.sleep(2)

driver.find_element(By.XPATH,'//span[@id="basic-addon1"]//parent::div//parent::div/input[@name="email"]').send_keys("mail@email.com")
time.sleep(2)

driver.find_element(By.XPATH,'//div[@class="input-group-prepend"]//following-sibling::input[@name="phone"]').send_keys("08902813480")
time.sleep(2)

driver.find_element(By.XPATH,'//button[contains(text(),"Book")]//preceding-sibling::button').click()
time.sleep(2)