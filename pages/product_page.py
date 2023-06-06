from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def execute_shopping_workflow(self):
        self.message_added_to_cart()
        self.product_actually_added()
        self.message_with_the_cost_of_the_cart()
        self.basket_cost_equals_product_price()

    def message_added_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), 'Товар не добавлен в корзину'

    def product_actually_added(self):
        assert self.equal_element(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME),
                                  self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)), 'f'

    def message_with_the_cost_of_the_cart(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE),'g'

    def basket_cost_equals_product_price(self):
        assert self.equal_element(self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE),
                                  self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)), 'fg'
