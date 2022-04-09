from decimal import Decimal as D
from .base_page import BasePage
from .locators import ProductPageLocators as PPL

class ProductPage(BasePage):
	def should_be_product_page(self):
		initial_basket_price = self.get_prod_price(*PPL.BASKET_TOTAL_PRICE)
		self.add_in_basket()
		self.solve_quiz_and_get_code()
		self.rigth_title_in_notice()
		self.rigth_price_in_basket(initial_basket_price)

	def add_in_basket(self):
		add_btn = self.browser.find_element(*PPL.ADD_TO_BASKET)
		add_btn.click()	

	def rigth_title_in_notice(self):
		book_title = self.get_element_text(*PPL.PROD_TITLE)
		notice_book_title = self.get_element_text(*PPL.NOTICE_PROD_TITLE)
		assert book_title in notice_book_title,\
		"Product title doesn't match in notice"

	def rigth_price_in_basket(self, initial):
		prod_price = self.get_prod_price(*PPL.PROD_PRICE)
		notice_basket_total_price = self.get_prod_price(*PPL.NOTICE_BASKET_TOTAL_PRICE)
		assert D(prod_price) == D(notice_basket_total_price) - D(initial),\
		"Product price doesn't match in notice"
