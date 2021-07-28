import time
from selenium.webdriver.common.action_chains import ActionChains


def test_action_chains(set_up):
    wd = set_up

    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    ActionChains(driver).click(anotation_body).drag_and_drop(alink_from, anotation_body).perform()
    wd.find_element_by_css_selector('#columns-full > div:nth-child(1) > div').click()

    time.sleep(5)
