from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

POPULAR_FILTERS = (By.CSS_SELECTOR, '[data-test="pic-nav-automation"] span h2')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
HEADER_TARGET = (By.CSS_SELECTOR, '[data-test="@web/HeaderPrimaryNav"]')

@given('Open target main page')
def step_impl(context):
    context.driver.get('https://www.target.com/')
    context.driver.wait.until(EC.visibility_of_element_located(HEADER_TARGET))

    # sleep(3)

@when ('click on the cart icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='/icons/Cart']").click()
    sleep(3)

@when('Search for {item}')
def search_product(context,item):
    context.driver.find_element(By.ID, 'search').send_keys(item)
    #context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN)).click()
    #sleep(5)
    context.driver.wait.until(EC.visibility_of_element_located(POPULAR_FILTERS))
    sleep(6)




