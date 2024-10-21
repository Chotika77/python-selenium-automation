from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

    def verify_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_HEADER)

    def verify_results_url(self, product):
        self.verify_partial_url(product)

    # def verify_cart_items(self, product):
    #     self.verify_partial_text(product,*self.CART_SUMMARY)

    def verify_cart_item(self,amount):
        self.verify_amount_item(amount,*self.CART_SUMMARY)