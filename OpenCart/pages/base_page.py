from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

by = None


class BasePage:
    global by

    def __init__(self, driver):
        self.driver = driver

    def __web_element(self, locator_dict: dict, index_dict: int, index_webelement: int):
        webelement_tuple = self.__webelement_tuple(locator_dict, index_dict)
        return self.driver.find_elements(webelement_tuple[0], webelement_tuple[1])[index_webelement]

    def __webelement_tuple(self, locator_dict: dict, index_dict: int):
        locator = list(locator_dict.keys())[index_dict]
        if locator == 'css':
            by = By.CSS_SELECTOR
        elif locator == 'xpath':
            by = By.XPATH
        elif locator == 'linc text':
            by = By.LINK_TEXT
        elif locator == 'id':
            by = By.ID
        return by, list(locator_dict.values())[index_dict]

    def _click(self, locator_dict: dict, index_dict: int = 0, index_webelement: int = 0):
        self.__web_element(locator_dict, index_dict, index_webelement).click()
        return self

    def _send_keys(self, keys: str, locator_dict: dict, index_dict: int = 0, index_webelement: int = 0):
        we = self.__web_element(locator_dict, index_dict, index_webelement)
        we.click()
        we.clear()
        we.send_keys(keys)
        return self

    def _wait_for_clickable(self, locator_dict: dict, index_dict: int = 0, wait: int = 3):
        webelement_tuple = self.__webelement_tuple(locator_dict, index_dict)
        return WebDriverWait(self.driver, wait) \
            .until(EC.element_to_be_clickable(webelement_tuple))
