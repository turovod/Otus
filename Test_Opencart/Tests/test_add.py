import time
from Test_Opencart.model.locators import get_by_btn_url


def test_a(set_up_t_down):
    wd = set_up_t_down

    by_btn_url = get_by_btn_url(2)
    wd.find_element_by_css_selector(by_btn_url).click()
    time.sleep(3)
    wd.find_element_by_id("cart-total").click()
    wd.find_element_by_css_selector('p.text-right > a > strong').click()

    assert wd.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[2]/a') \
           .text == 'iPhone', 'Not Iphone'

    time.sleep(10)
