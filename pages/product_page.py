from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def click_add_to_cart(self):
        self.wait_to_be_clickable_click(*self.ADD_TO_CART_BTN)

    def side_nav_click_add_to_cart(self):
        self.wait_to_be_clickable_click(*self.ADD_TO_CART_BTN_SIDE_NAV)

