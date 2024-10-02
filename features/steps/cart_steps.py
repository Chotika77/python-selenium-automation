from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CONT_SHOP = (By.XPATH, "//*[text() = 'Continue shopping']")



@then('I should see the message "Your cart is empty"')
def step_impl1(context):
    context.driver.find_element(By.CSS_SELECTOR,".dtCtuk")
    sleep(3)

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    (context.driver.wait.until
     (EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
      message = 'side navigation product name not visible'))

# @when('Store product name')
# def store_product_name(context):
#     context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
#     print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    context.driver.wait.until(EC.visibility_of_element_located(CONT_SHOP))


    # sleep(3)


@when ('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')




@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
