from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    #CART_BTN = (By.CSS_SELECTOR, "[href*='/icons/Cart']")
    CART_BTN = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        #self.input_text(*self.SEARCH_FIELD, text=product)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def cart_icon(self):
        self.click(*self.CART_BTN)
        sleep(3)
