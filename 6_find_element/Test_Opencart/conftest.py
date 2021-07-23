import pytest
from selenium import webdriver


@pytest.fixture
def initial_test(request):
    if request.config.getoption('--brouser') == 'C':
        driver = webdriver.Chrome(executable_path='/Users/s.loginov/Desktop/Otus/5_Test_Opencart/drivers/chromedriver')
        driver.get('http://localhost:8888/opencart3/upload/')
        driver.fullscreen_window()

    if request.config.getoption('--brouser') == 'F':
        driver = webdriver.Firefox(executable_path='/Users/s.loginov/Desktop/Otus/5_Test_Opencart/drivers/geckodriver')
        driver.get('http://localhost:8888/opencart3/upload/')

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--brouser",
        help="Config brauser, defaults to %(default)s",
        default='C',
    )
