from re import search
from math import log, sin
from .locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

class BasePage:    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_element_text(self, how, what):
        text = self.browser.find_element(how, what).text
        return text

    def get_prod_price(self, how, what):
        expression = self.get_element_text(how, what)
        expression = expression.replace(",", ".")
        price = search(r'(\d+.\d+)', expression)
        return price.group(0)

    def click_to(self, how, what):
        click_object = self.browser.find_element(how, what)
        click_object.click()

    def go_to_basket_page(self):
        self.click_to(*BasePageLocators.BASKET_LINK)

    def go_to_login_page(self):
        self.click_to(*BasePageLocators.LOGIN_LINK)

    def send_keys_to(self, how, what_elem, what_send):
        send_to_object = self.browser.find_element(how, what_elem)
        send_to_object.send_keys(what_send)

    def should_be_autorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON),\
        "User icon is not presented, probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
        "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        
        except NoSuchElementException:
            return False
        
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WDW(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        
        except TimeoutException:
            return True
        
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WDW(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))

        except TimeoutException:
            return False

        return True
