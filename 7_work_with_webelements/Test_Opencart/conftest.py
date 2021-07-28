import time

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def set_up_t_down(request):
    drivers_path = __file__
    drivers_path = drivers_path.replace('conftest.py', '')
    drivers_path += 'Drivers'
    if request.config.getoption('--browser') == 'Chrome':
        driver = webdriver.Chrome(executable_path=drivers_path + '/chromedriver')
    driver.get("http://localhost:8888/opencart3/upload/")
    driver.fullscreen_window()
    time.sleep(3)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='--browser=choose',
        default='Chrome'
    )
