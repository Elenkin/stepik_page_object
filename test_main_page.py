from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


""" PyTest --tb=line, выводит только одну строку из лога каждого упавшего теста """


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # переход с главной страницы в корзину
    # и проверка что в корзине нет товаров и есть сообщение что корзина пуста
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_items_in_basket()
    basket_page.should_be_text_about_empty_basket()
