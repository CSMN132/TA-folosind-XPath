import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://carturesti.ro/")

driver.find_element(By.XPATH,'//a[@aria-label="allow cookies"]').click()# time.sleep(2)

driver.find_element(By.XPATH,'//button/a').click()

city_select = Select(driver.find_element(By.XPATH,'//select[@id="city_select_id"]'))
city_select.select_by_visible_text("Baia Mare")

time.sleep(2)

try:
    driver.find_element(By.XPATH,'//h3[contains(text(),"Carturesti Baia Mare")]')
except NoSuchElementException:
    assert False, "Nu a aparut elementul dorit cand am ales orasul Baia Mare"

time.sleep(2)