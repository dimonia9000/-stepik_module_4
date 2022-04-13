from decimal import Decimal as D
from .base_page import BasePage
from .locators import ProductPageLocators as PPL

class ProductPage(BasePage):
	def should_be_in_product_page(self):
		initial_basket_price = self.get_prod_price(*PPL.BASKET_TOTAL_PRICE)
		self.add_in_basket()
		if "promo" in self.url:
			self.solve_quiz_and_get_code()
		self.rigth_title_in_notice()
		self.rigth_price_in_basket(initial_basket_price)

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*PPL.SUCCESS_MESSAGE),\
		"Success message is presented but should not be"

	def should_be_disappeared_success_message(self):
		assert self.is_disappeared(*PPL.SUCCESS_MESSAGE),\
		"Success message is presented but should be disappeared"
	
	def add_in_basket(self):
		self.click_to(*PPL.ADD_TO_BASKET)
		

	def rigth_title_in_notice(self):
		book_title = self.get_element_text(*PPL.PROD_TITLE)
		notice_book_title = self.get_element_text(*PPL.NOTICE_PROD_TITLE)
		assert book_title == notice_book_title,\
		f"Product title({book_title}) doesn't match in notice({notice_book_title})"

	def rigth_price_in_basket(self, initial):
		prod_price = self.get_prod_price(*PPL.PROD_PRICE)
		notice_basket_total_price = self.get_prod_price(*PPL.NOTICE_BASKET_TOTAL_PRICE)
		assert D(prod_price) == D(notice_basket_total_price) - D(initial),\
		"Product price doesn't match in notice"
