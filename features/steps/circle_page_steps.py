from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Target Circle')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,"#utilityNav-circle").click()

@then('10 benefit cells are shawn')
def verify_b_cells(context):
    b_cells = context.driver.find_elements(By.CSS_SELECTOR,".cell-item-content")
    print(b_cells)
    assert len(b_cells) == 10, f"expected 10 b_cells, got {len(b_cells)}"
