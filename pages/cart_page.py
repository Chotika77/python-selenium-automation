from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    SEARCH_RESULTS_CART = (By.CSS_SELECTOR,".dtCtuk")

    def verify_empty_cart(self):
        self.verify_text("Your cart is empty", *self.SEARCH_RESULTS_CART)

    def open_cart(self):
        self.driver.get('https://www.target.com/cart')

