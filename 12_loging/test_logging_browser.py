import pytest
from selenium import webdriver

from OpenCart.Drivers import get_driver_path


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option('w3c', False)
    driver_path = get_driver_path()
    wd = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_logging_browser(chrome_browser):

    chrome_browser.get('https://www.searchengines.ru/search-console-fix.html')
    print('==============', chrome_browser.log_types)
    for l in chrome_browser.get_log("browser"):
        print('==============', l)


