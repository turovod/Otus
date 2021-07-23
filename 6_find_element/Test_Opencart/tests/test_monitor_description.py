import time


def test_monitor_description(initial_test):
    driver = initial_test

    driver.find_element_by_link_text('Components').click()
    time.sleep(2)
    driver.find_element_by_partial_link_text('Monitors').click()
    time.sleep(2)
    assert driver.find_element_by_css_selector('div.caption > h4 > a').text == 'Apple Cinema 30"'
