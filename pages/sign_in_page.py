from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_PAGE = (By.XPATH, "//span[text()='Sign into your Target account']")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")


    def open_sign_in_page(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def click_tc_link(self):
        self.wait_to_be_clickable_click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/')


    def verify_sign_in_form(self):
        self.wait_for_element_to_appear(*self.SIGN_IN_PAGE)





