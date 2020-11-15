from .locators import ProductPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_not_items_in_basket(self):
        # проверка что в корзине нет товара
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ITEMS), "ERROR! Basket not empty"

    def should_be_text_about_empty_basket(self):
        # проверка наличия сообщения что корзина пуста
        text = self.browser.find_element(*ProductPageLocators.EMPTY_BASKET_MESSAGE).text
        print(text)
        assert "Your basket is empty." in text, "ERROR! Not message basket empty"