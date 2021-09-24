import time
from OpenCart.locators import Login
from OpenCart.pages import CommonPage, LoginLogout


def test_login(setup_teardown):
    driver = setup_teardown[0]
    logger = setup_teardown[1]
    logger.info('TEST START')
    CommonPage(driver)\
        .go_to_login_page()\
        ._wait_for_clickable(Login.login_email)
    LoginLogout(driver).login_user('turovodspb@gmail.com', 'Tur0v0d1')
    logger.info('TEST PASSED')
    # driver.find_element_by_xpath('ggg').click()

