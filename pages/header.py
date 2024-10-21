from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    #CART_BTN = (By.CSS_SELECTOR, "[href*='/icons/Cart']")
    CART_BTN = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    SIGN_IN_BTN = (By.CSS_SELECTOR, "span.h-margin-r-x3")
    SIGN_IN_NAV_BTN = (By.CSS_SELECTOR, ".hHZPQy")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        #self.input_text(*self.SEARCH_FIELD, text=product)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def cart_icon(self):
        self.wait_to_be_clickable_click(*self.CART_BTN)


    def sign_in_icon(self):
        self.click(*self.SIGN_IN_BTN)

    def sign_in_nav_icon(self):
        self.wait_to_be_clickable_click(*self.SIGN_IN_NAV_BTN)





