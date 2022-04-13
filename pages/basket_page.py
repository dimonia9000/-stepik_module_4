from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_empty_basket_text(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT),\
		"No basket empty text"

	def should_not_be_item_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.PROD_IN_BASKET),\
		"Basket not empty"
