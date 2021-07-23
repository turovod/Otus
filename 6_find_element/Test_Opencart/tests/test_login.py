import time


def test_login(initial_test):
    driver = initial_test
    driver.find_element_by_css_selector("a.dropdown-toggle > span.hidden-xs.hidden-sm.hidden-md")\
        .click()
    driver.find_element_by_link_text('Login').click()
    click_clear_send_keys_by_css(driver, '#input-email', 'serge@gmail.com')
    click_clear_send_keys_by_css(driver, '#input-password', '1111')
    driver.find_element_by_css_selector('input.btn.btn-primary').click()

    assert driver.find_element_by_css_selector('#content > h2:nth-child(1)').text == 'My Account'


def click_clear_send_keys_by_id(driver, locator, keys):
    driver.find_element_by_id(locator).click()
    driver.find_element_by_id(locator).clear()
    driver.find_element_by_id(locator).send_keys(keys)


def click_clear_send_keys_by_css(driver, locator, keys):
    driver.find_element_by_css_selector(locator).click()
    driver.find_element_by_css_selector(locator).clear()
    driver.find_element_by_css_selector(locator).send_keys(keys)