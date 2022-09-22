from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_items()
        self.should_be_message()

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket should be empty, but it is not"

    def should_be_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)
        assert "Your basket is empty" in basket_message.text, \
            "Should be message about basket emptiness, but there is not"
