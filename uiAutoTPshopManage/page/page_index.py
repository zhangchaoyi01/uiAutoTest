import page
from base.base_page import BasePage


class PageIndex(BasePage):

    def page_get_admin_text(self):
        return self.base_text(page.admin_text)

    def page_click_shop_btn(self):
        self.base_click(page.shop_btn)