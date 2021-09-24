import time

import pytest
from selenium import webdriver

from OpenCart.Drivers import get_driver_path


@pytest.fixture
def set_test():
    # wd = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities={'browserName': 'chrome', 'version': '', 'platform': 'ANY'})
    wd = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities={'browserName': 'chrome'})
    # wd = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.CHROME)
    # wd = webdriver.Chrome(executable_path=get_driver_path())
    yield wd
    wd.close()


def test_a(set_test):
    wd = set_test
    wd.get('https://www.google.com/')
    time.sleep(5)
