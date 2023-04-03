from page.page_index import PageIndex
from page.page_login import PageLogin
from page.page_shop import PageShop


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    def page_get_PageLogin(self):
        return PageLogin(self.driver)

    def page_get_PageIndex(self):
        return PageIndex(self.driver)

    def page_get_PageShop(self):
        return PageShop(self.driver)

