import time
from selenium.webdriver.common.action_chains import ActionChains


def test_action_chains(set_up):
    wd = set_up

    anotation_body = wd.find_element_by_id('drag1')
    alink_from = wd.find_element_by_id("div2")

    time.sleep(3)

    ActionChains(wd).click(alink_from).drag_and_drop(source=anotation_body, target=alink_from).perform()

    time.sleep(5)
