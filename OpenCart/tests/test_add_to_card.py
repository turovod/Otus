import time

from OpenCart.pages import CommonPage, MainPage, BasePage


def test_add(setup_teardown):
    driver = setup_teardown
    MainPage(driver).add_to_card_by_index('2')
    driver.fullscreen_window()
    time.sleep(1)
    CommonPage(driver)\
        .open_shopping_cart()\
        .go_to_view_cart_page()
    dic = {'linc text': 'iPhone'}
    BasePage(driver)._wait_for_clickable(dic)

