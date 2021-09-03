import time
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.keys import Keys

from OpenCart.Drivers import get_driver_path


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = EventFiringWebDriver(webdriver.Chrome(executable_path=get_driver_path()), MyListener())
    request.addfinalizer(wd.quit)
    return wd


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        logging.log(msg="Hello, Before find!")
        print(by, value)

    def after_find(self, by, value, driver):
        pass
        #print(by, value, "found")

    def on_exception(self, exception, driver):
        # pass
        driver.save_screenshot('screenshots/exception.png')
        #print(exception)


def test_logging(chrome_browser):
    chrome_browser.get('https://habr.com/ru/company/skyeng/blog/465291/')
    find_button = chrome_browser.find_element_by_id('.search-form-btn12345')
    find_button.click()
    # find_field = chrome_browser.find_element_by_id('search-form-field')
    # find_field.send_keys('Otus')
    logging.log(1, 'opened list of posts')
    # find_field.send_keys(Keys.ENTER)
    chrome_browser.save_screenshot('screenshots/finish_test.png')
