import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from OpenCart.Drivers import get_driver_path


@pytest.fixture
def chrome_browser(request):
    d = DesiredCapabilities.CHROME
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('w3c', False)
    d['loggingPrefs'] = {'performance': 'ALL'}
    driver_path = get_driver_path()
    wd = webdriver.Chrome(executable_path=driver_path, desired_capabilities=d, chrome_options=opt)
    request.addfinalizer(wd.quit)
    return wd


def test_logging_browser(chrome_browser):

    chrome_browser.get('https://otus.ru/')
    print(chrome_browser.log_types)
    lst = chrome_browser.get_log("performance")
    for l in lst:
        print(l)