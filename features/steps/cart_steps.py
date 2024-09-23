from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('I should see the message "Your cart is empty"')
def step_impl1(context):
    context.driver.find_element(By.CSS_SELECTOR,".dtCtuk")
    sleep(3)

@when('add product to cart')
def add_to_cart(context):
    context.driver.find_element(By.XPATH,"//div[@data-test='@web/site-top-of-funnel/ProductCardWrapper']//button[@data-test='chooseOptionsButton']").click()

    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor52001650").click()

@when('view cart')
def view_cart(context):
    context.driver.find_element(By.XPATH, "//div[text()='View cart & check out']")
    sleep(2)








