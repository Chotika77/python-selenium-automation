from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

sleep(3)
# by CSS, by class
# driver.find_element(By.CSS_SELECTOR,".nav-input")
# by CSS, by tag and class(es)
# driver.find_element(By.CSS_SELECTOR, "input.nav-input")

# driver.find_element(By.CSS_SELECTOR,'("[placeholder='Search Amazon']")'

driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")