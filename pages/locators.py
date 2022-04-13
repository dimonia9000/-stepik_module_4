from selenium.webdriver.common.by import By

class BasePageLocators():
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
	PROD_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
class LoginPageLocators():
	CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
	LOGIN_FORM = (By.ID, "login_form")
	PASSWORD = (By.ID, "id_registration-password1")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
	REGISTER_EMAIL = (By.ID, "id_registration-email")
	REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
	BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-mini")
	PROD_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
	NOTICE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR,\
		"#messages > :nth-child(3) > :nth-child(2) strong")
	PROD_TITLE = (By.CSS_SELECTOR, ".product_main h1")
	NOTICE_PROD_TITLE = (By.CSS_SELECTOR,\
		"#messages > :nth-child(1) > :nth-child(2) > strong")
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
