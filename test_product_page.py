from .pages.product_page import ProductPage
import pytest        # необходимо будет убрать, т.к. уже есть импорт в conftest, сейчас нужна чтобы PC не ругался
from .pages.login_page import LoginPage


@pytest.mark.parametrize(
    'link', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
             pytest.param("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                          marks=pytest.mark.xfail),
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_an_opportunity_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_price_and_name()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_an_opportunity_add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_an_opportunity_add_product_to_basket()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()