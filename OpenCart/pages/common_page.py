from .base_page import BasePage
from OpenCart.locators import Common


class CommonPage(BasePage):

    def open_my_account(self):
        self._click(Common.TopMenu.my_account)
        return self

    def open_shopping_cart(self):
        self._click(Common.Header.shopping_cart)
        return self

    def go_to_login_page(self):
        self.open_my_account()
        self._click(Common.TopMenu.login)
        self.driver.fullscreen_window()
        return self

    def go_to_main_page(self):
        self._click(Common.Navigation.main_page)
        self.driver.fullscreen_window()
        return self

    def go_to_view_cart_page(self):
        self._click(Common.Header.view_cart)
        self.driver.fullscreen_window()
        return self

    def go_to_wish_list_authorized(self):
        self._click(Common.Header.wish_list)
