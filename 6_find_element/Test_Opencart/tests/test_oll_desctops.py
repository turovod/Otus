import selenium


def test_oll_desktops(initial_test):
    driver = initial_test
    driver.find_element_by_link_text('Desktops').click()
    driver.find_element_by_link_text('Show AllDesktops').click()
    group_list = driver.find_elements_by_css_selector('div.list-group > a')
    assert len(group_list) == 10
