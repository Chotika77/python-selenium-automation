from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    SEARCH_RESULTS_CART = (By.CSS_SELECTOR,".dtCtuk")

    def verify_empty_cart(self,text):
        actual_result = self.driver.find_element(*self.SEARCH_RESULTS_CART).text
        assert text in actual_result, f"Expected {text}, got actual {actual_result}"
        sleep(3)