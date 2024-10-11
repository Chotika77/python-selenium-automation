from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

# @then('Verify that correct search results shown for {product}')
# def verify_results(context,product):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert product in actual_result, f"Expected {expected_result}, got actual {actual_result}"
#     sleep(3)

@then('Verify that correct search results shown for {product}')
def verify_results(context,product):
    # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # assert product in actual_result, f"Expected {product}, got actual {actual_result}"
    context.app.search_results_page.verify_results(product)

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)