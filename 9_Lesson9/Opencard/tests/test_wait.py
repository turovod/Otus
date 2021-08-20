import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_wait(fixture_tests):
    wd = fixture_tests
    login_path = '#top-links ul.list-inline li.dropdown a.dropdown-toggle span.hidden-xs'
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_path))).click()

    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))).click()

    wd.fullscreen_window()

    wd.find_element_by_id('input-email').click()
    wd.find_element_by_id('input-email').clear()
    wd.find_element_by_id('input-email').send_keys('turovodspb@gmail.com')

    wd.find_element_by_id('input-password').click()
    wd.find_element_by_id('input-password').clear()
    wd.find_element_by_id('input-password').send_keys('turovodspb@gmail.com')

    time.sleep(2)

    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn-primary'))).click()

    time.sleep(5)
