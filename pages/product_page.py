from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_button()
        self.should_be_success_message()
        self.should_be_correct_basket_price()

    def should_be_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        success_message = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        assert product_name.text == success_message[0].text, "Success message doesn't contain name of added product"

    def should_be_correct_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_elements(*ProductPageLocators.BASKET_PRICE)
        assert product_price.text == basket_price[2].text, "Total basket price doesn't match added product price"
