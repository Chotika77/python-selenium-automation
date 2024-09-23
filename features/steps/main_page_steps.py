from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def step_impl(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when ('click on the cart icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='/icons/Cart']").click()
    sleep(3)

@when('Search for {item}')
def search_product(context,item):
    context.driver.find_element(By.ID, 'search').send_keys(item)

    sleep(6)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(3)
git