import unittest
from parameterized import parameterized
from base.base_page import BasePage
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_order_search_json import get_data


class TestOrderSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        driver = GetDriver.get_driver()
        cls.page_in_shop = PageIn(driver).page_get_PageShop()
        page_in_login = PageIn(driver).page_get_PageLogin()
        page_in_index = PageIn(driver).page_get_PageIndex()
        cls.base_page = BasePage(driver)

        # 登录
        page_in_login.login_success()
        # 点击商城
        page_in_index.page_click_shop_btn()
        # 点击订单
        cls.page_in_shop.page_click_order()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_driver()

    @parameterized.expand(get_data("order_search.json"))
    def test_order_search(self, time_begin, time_end,
                          select, loc_01, loc_02, loc_03, loc_04):
        # 订单列表筛选
        self.page_in_shop.page_search_order(time_begin, time_end, select,
                                            loc_01, loc_02, loc_03, loc_04)
