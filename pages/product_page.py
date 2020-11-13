from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def check_result_messages(self):
        self.check_message_about_basket()
        self.check_name_book_in_basket()
        self.check_price_book_in_basket()

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON).click()

    def should_be_add_basket_button(self):
        # проверка наличия кнопки "добавить в корзину"
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Page not contains ADD_BASKET_BUTTON"

    def add_result(self):
        # получение проверочного кода
        self.solve_quiz_and_get_code()

    def check_price_book_in_basket(self):
        # проверка что Стоимость корзины совпадает с ценой товара
        price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BOOK).text
        assert price == price_in_basket, "ERROR! Different price"

    def check_name_book_in_basket(self):
        # проверка что Название товара в сообщении совпадает с добавленным
        name = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        name_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_BOOK).text
        assert name in name_in_basket, "ERROR! Basket not contains this book"

    def check_message_about_basket(self):
        # проверка наличия сообщения что товары добавлены в корзину
        assert self.is_element_present(*ProductPageLocators.TEXT_MESSAGE), "ERROR! Message is not presented"