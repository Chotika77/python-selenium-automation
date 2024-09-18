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
driver.get('https://www.amazon.com/ap/register?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Freport%2Finfringement&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_noticeform_desktop_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(10)


driver.find_element(By.CSS_SELECTOR,  ".a-icon.a-icon-logo[aria-label='Amazon']")


driver.find_element(By.CSS_SELECTOR, " .a-spacing-small")

driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")

driver.find_element(By.CSS_SELECTOR,"#ap_email")

driver.find_element(By.CSS_SELECTOR, "#ap_password")

driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

driver.find_element(By.CSS_SELECTOR, "#continue")

driver.find_element(By.CSS_SELECTOR,"[href*='condition of use']")

driver.find_element(By.CSS_SELECTOR, "[href*='Privacy Notice']")

driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")

