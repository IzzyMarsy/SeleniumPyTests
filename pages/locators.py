from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTR = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main h1+p")

    ADD_TO_BASKET = (By.CSS_SELECTOR, "[value='Добавить в корзину']")

    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-last-child(3) strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-last-child(1) strong")
