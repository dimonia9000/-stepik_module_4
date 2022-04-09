from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.ID, "login_form")
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