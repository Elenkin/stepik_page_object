from selenium.webdriver.common.by import By


#каждый селектор — это пара: как искать и что искать
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#lid_registration-email")
    PASSWORD1_INPUT = (By.CSS_SELECTOR, "id_registration-password1")
    PASSWORD2_INPUT = (By.CSS_SELECTOR, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.ID, "login_form")
    USERNAME_INPUT = (By.CSS_SELECTOR, "id_login-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")
    MESSAGE_NAME_BOOK = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    MESSAGE_PRICE_BOOK = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset .basket-items")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")
