import time

import pytest
from selenium import webdriver


@pytest.fixture
def setup_teardown(request):
    if request.config.getoption("--brouser") == 'Chrome':
        options = None
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(
            executable_path="/5_Test_Opencart/drivers/chromedriver",
            options=options)
        driver.get('http://localhost:8888/opencart3/upload/')
        driver.fullscreen_window()

    if request.config.getoption("--brouser") == 'Firefox':
        options = None
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Firefox(
            executable_path="/5_Test_Opencart/drivers/geckodriver",
            options=options)
        driver.get('http://localhost:8888/opencart3/upload/')
        driver.fullscreen_window()
    else:
        print('*' * 50 + '\nHello')

    time.sleep(3)
    # request.addfinalizer(lambda: driver.quit())
    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--brouser",
        help="Config brauser, defaults to %(default)s",
        default='Firefox',
    )
