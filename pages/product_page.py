from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket_quiz(self):
        self.should_be_add_button()
        self.solve_quiz_and_get_code()
        self.should_be_success_message()
        self.should_be_correct_basket_price()

    def add_product_to_basket(self):
        self.should_be_add_button()
        self.should_be_success_message()
        self.should_be_correct_basket_price()

    def should_be_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert product_name.text == success_message.text, "Success message doesn't contain name of added product"

    def should_be_correct_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price.text == basket_price.text, "Total basket price doesn't match added product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it is not"
