from .base_page import BasePage
from OpenCart.locators import Main


class MainPage(BasePage):
    def add_to_card_by_index(self, number_featured: str, index_locator: int = 0):

        locator_dict = {
            list(Main.add_to_cart.keys())[index_locator]:
            list(Main.add_to_cart.values())[index_locator].replace('index', number_featured)
        }
        self._click(locator_dict)
        return self

    def add_to_wish_list(self):
        self._click(Main.add_to_wish_list_path)
        return self



