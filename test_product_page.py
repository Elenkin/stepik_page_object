import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('part', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                  pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, part):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo={part}"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_add_basket_button()
    product_page.add_to_basket()
    product_page.add_result()
    time.sleep(2)
    product_page.check_result_messages()
