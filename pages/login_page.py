from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not 'login' in link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
        f"Not find {LoginPageLocators.LOGIN_FORM} element"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),\
        f"Not find {LoginPageLocators.REGISTER_FORM} element"

    def register_new_user(self, email, password):
        self.send_keys_to(*LoginPageLocators.REGISTER_EMAIL, email)
        self.send_keys_to(*LoginPageLocators.PASSWORD, password)
        self.send_keys_to(*LoginPageLocators.CONFIRM_PASSWORD, password)
        self.click_to(*LoginPageLocators.REGISTER_BUTTON)
