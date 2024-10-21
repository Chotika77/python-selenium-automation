from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open target main page')
# def step_impl(context):
#     context.driver.get('https://www.target.com/')
#     sleep(3)

#
# @when('Search for a product')
# def search_product(context):
#     context.driver.find_element(By.ID, 'search').send_keys('tea')

    # sleep(6)
    # context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # sleep(3)


@then('Verify that correct search results are shown')
def verify_results(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    expected_result = 'tea'
    assert expected_result in actual_result, f"Expected {expected_result}, got actual {actual_result}"
    sleep(3)

# @when ('click on the cart icon')
# def step_impl(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[href*='/icons/Cart']").click()
#     sleep(3)




@when('click on the Sign In icon')
def sign_in(context):
    context.app.header.sign_in_icon()

@when('click on the Sign In button from the right-side navigation menu')
def sign_in1(context):
    context.app.header.sign_in_nav_icon()


@then('The expected outcome is seeing the Sign In form')
def verify_results(context):
    # context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
    context.app.sign_in_page.verify_sign_in_form()
















