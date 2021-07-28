from ..locators import MainPage, CatalogPage
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


def test_select_value(browser):
    Bro = browser

    desktops_link = Bro.find_element(*MainPage.menu.desktops.link)
    ActionChains(Bro).move_to_element(desktops_link).pause(2).perform()
    Bro.find_element(*MainPage.menu.desktops.show_all).click()

    # StaleReferenceException
    select_limit = Select(Bro.find_element(*CatalogPage.select_limit))
    select_limit.select_by_visible_text("100")

    select_limit = Select(Bro.find_element(*CatalogPage.select_limit))
    assert select_limit.first_selected_option.text == "100"
