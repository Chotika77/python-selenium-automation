from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.target.com/')

sleep(2)

driver.find_element(By.XPATH,"//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()

sleep(2)

driver.find_element(By.XPATH,"//span[@class='sc-859e7637-0 hHZPQy']").click()

sleep(2)

driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']")

sleep(2)

driver.find_element(By.XPATH,"//span[text()='Sign in with password']")

driver.quit()