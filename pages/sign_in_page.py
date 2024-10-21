from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_PAGE = (By.XPATH, "//span[text()='Sign into your Target account']")


    def verify_sign_in_form(self):
        self.wait_for_element_to_appear(*self.SIGN_IN_PAGE)





