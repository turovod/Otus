import time

from OpenCart.pages import MainPage, CommonPage, BasePage


def test_remove_from_cart(setup_teardown):
    driver = setup_teardown
    MainPage(driver).add_to_card_by_index('2')
    driver.fullscreen_window()
    time.sleep(1)
    CommonPage(driver) \
        .open_shopping_cart() \
        .go_to_view_cart_page()
    dic = {'linc text': 'iPhone'}
    BasePage(driver)._wait_for_clickable(dic)
    for _ in range(10):
        if driver.find_elements_by_xpath('//*[@id="content"]//td[4]//button[2]'):
            driver.find_element_by_xpath('//*[@id="content"]//td[4]//button[2]').click()
            time.sleep(1)
        else:
            break

    assert len(driver.find_elements_by_link_text('iPhone')) == 0

