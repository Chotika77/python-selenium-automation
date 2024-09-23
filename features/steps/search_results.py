from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify that correct search results shown for {product}')
def verify_results(context,product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f"Expected {expected_result}, got actual {actual_result}"
    sleep(3)

@then('Verify that correct search results shown for {product}')
def verify_results(context,product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f"Expected {product}, got actual {actual_result}"

@then('Verify product is shawn in the cart')
def verify_item_in_cart(context):
    expected_text = 1 item
    actual_result = context.driver.find_element(By.CSS_SELECTOR,".fUVkzh").text
    assert expected_text == actual_result, f"Expected {expected_text}, got actual {actual_result}"