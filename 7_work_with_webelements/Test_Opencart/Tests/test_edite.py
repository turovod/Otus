import time
from Test_Opencart.model.locators import get_by_btn_url


def test_a(set_up_t_down):
    wd = set_up_t_down

    # driver = set_up_t_down
    # driver.get("http://localhost:8888/opencart3/upload/index.php?route=common/home")
    # driver.find_element_by_xpath(
    #     "//div[@id='content']/div[2]/div[2]/div/div[3]/button/span").click()
    # time.sleep(3)
    # driver.find_element_by_id("cart-total").click()
    # driver.find_element_by_xpath("//div[@id='cart']/ul/li[2]/div/p/a/strong").click()
    # time.sleep(3)
    # driver.find_element_by_xpath(
    #     "//div[@id='content']/form/div/table/tbody/tr/td[4]/div/input").click()
    # driver.find_element_by_xpath(
    #     "//div[@id='content']/form/div/table/tbody/tr/td[4]/div/input").clear()
    # driver.find_element_by_xpath(
    #     "//div[@id='content']/form/div/table/tbody/tr/td[4]/div/input").send_keys("55")
    # driver.find_element_by_xpath(
    #     "//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button/i").click()

    by_btn_url = get_by_btn_url(2)
    wd.find_element_by_css_selector(by_btn_url).click()
    time.sleep(3)
    wd.find_element_by_id("cart-total").click()
    wd.find_element_by_css_selector('p.text-right > a > strong').click()
    time.sleep(5)
    wd.find_element_by_xpath(
        "//div[@id='content']/form/div/table/tbody/tr/td[4]/div/input").click()
    wd.find_element_by_xpath(
        "//div[@id='content']/form/div/table/tbody/tr/td[4]/div/input").clear()
    wd.find_element_by_xpath(
        "//div[@id='content']/form/div/table/tbody/tr/td[4]/div/input").send_keys("55")
    wd.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]/i').click()


    time.sleep(5)