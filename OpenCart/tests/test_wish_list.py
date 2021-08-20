import time

from OpenCart.locators import Login
from OpenCart.pages import CommonPage, MainPage, LoginLogout


def test_wish_list(setup_teardown):
    driver = setup_teardown
    MainPage(driver).add_to_wish_list()
    CommonPage(driver) \
        .go_to_login_page() \
        ._wait_for_clickable(Login.login_email)
    LoginLogout(driver).login_user('turovodspb@gmail.com', 'Tur0v0d1')
    CommonPage(driver).go_to_wish_list_authorized()
    mac_book_path = '//*[@id="content"]//tr/td[2]/a'
    assert driver.find_element_by_xpath(mac_book_path).text == 'MacBook'
