def test_get_main_page(initial_test):
    driver = initial_test
    text_logo = driver.find_element_by_css_selector('#logo').text

    assert text_logo == 'Your Store'