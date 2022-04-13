import pytest
from time import time
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",\
                                  	marks=pytest.mark.skip),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.should_be_in_product_page()

link = "http://selenium1py.pythonanywhere.com/catalogue/we-are-anonymous_192/"
login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class TestUserAddToBasketFromProductPage:
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		email, password = str(time())+"@fakegpost.py", "KaDaBrAAAbRa1!"
		self.login_page = LoginPage(browser, login_link)
		self.login_page.open()
		self.login_page.register_new_user(email, password)
		self.login_page.should_be_autorized_user()
	
	@pytest.mark.need_review	
	def test_user_can_add_product_to_basket(self, browser):
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_be_in_product_page()

	def test_user_cant_see_success_message(self, browser):
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_item_in_basket()
    basket_page.should_be_empty_basket_text()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_in_basket()
	product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_in_basket()
	product_page.should_be_disappeared_success_message()
