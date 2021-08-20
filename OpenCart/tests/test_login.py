import time
from OpenCart.locators import Login
from OpenCart.pages import CommonPage, LoginLogout


def test_login(setup_teardown):
    driver = setup_teardown
    CommonPage(driver)\
        .go_to_login_page()\
        ._wait_for_clickable(Login.login_email)
    LoginLogout(driver).login_user('turovodspb@gmail.com', 'Tur0v0d1')
    time.sleep(3)

