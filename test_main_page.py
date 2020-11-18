import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


""" PyTest --tb=line, выводит только одну строку из лога каждого упавшего теста """


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        self.page.open()  # открываем страницу
        self.page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # переход с главной страницы в корзину
        # и проверка что в корзине нет товаров и есть сообщение что корзина пуста
        self.link = "http://selenium1py.pythonanywhere.com"
        self.page = BasketPage(browser, self.link)
        self.page.open()
        self.page.open_basket()
        self.basket_page = BasketPage(browser, browser.current_url)
        self.basket_page.should_be_not_items_in_basket()
        self.basket_page.should_be_text_about_empty_basket()
