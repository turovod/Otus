def test_first(setup_teardown):
    text_logo = setup_teardown.find_element_by_id('logo').text

    assert text_logo == 'Your Store'
