import time


def test_do_register(initial_test):
    driver = initial_test
    driver.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a/span").click()
    driver.find_element_by_link_text('Register').click()
    click_clear_send_keys(driver, "input-firstname", "Serge1")
    click_clear_send_keys(driver, "input-lastname", 'Loginoff1')
    click_clear_send_keys(driver, "input-email", 'serge1@gmail.com')
    click_clear_send_keys(driver, "input-telephone", '111-11-11')
    click_clear_send_keys(driver, "input-telephone", '111-11-11')
    click_clear_send_keys(driver, "input-password", '1111')
    click_clear_send_keys(driver, "input-confirm", '1111')
    driver.find_element_by_name('agree').click()
    driver.find_element_by_class_name('btn-primary').click()

    assert driver.find_element_by_css_selector("#content > p").text == 'Congratulations! ' \
                                                                       'Your new account has ' \
                                                                       'been successfully created!'


def click_clear_send_keys(driver, locator, keys):
    driver.find_element_by_id(locator).click()
    driver.find_element_by_id(locator).clear()
    driver.find_element_by_id(locator).send_keys(keys)


