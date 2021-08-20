from OpenCart.locators import Login
from .base_page import BasePage


class LoginLogout(BasePage):

    def login_user(self, email, password):
        self._send_keys(email, Login.login_email) \
            ._send_keys(password, Login.password) \
            ._click(Login.login_btn) \
            .driver.fullscreen_window()
        return self

