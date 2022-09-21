from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner strong")
