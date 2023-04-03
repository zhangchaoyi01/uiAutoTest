import page
from base.base_page import BasePage
from time import sleep
from tools.get_log import GetLogging

log = GetLogging.get_logger()


class PageShop(BasePage):

    def page_click_order(self):
        self.base_click(page.order_btn)

    def page_input_time_begin(self, time_begin):
        # 输入时间
        self.base_input(page.time_begin, time_begin)

    def page_input_time_end(self, time_end):
        self.base_input(page.time_end, time_end)

    def page_select_pay_satus(self, sele, loc_01):
        self.base_select_find(page.pay_status, sele, loc_01)

    def page_select_pay_code(self, sele, loc_02):
        self.base_select_find(page.pay_code, sele, loc_02)

    def page_select_shipping_status(self, sele, loc_03):
        self.base_select_find(page.shipping_status, sele, loc_03)

    def page_select_order_status(self, sele, loc_04):
        self.base_select_find(page.order_status, sele, loc_04)

    def page_click_search_btn(self):
        self.base_click(page.search_btn)

    def page_get_no_data(self):
        return self.base_text(page.no_data)

    def page_click_refresh_btn(self):
        self.base_click(page.refresh)

    def page_search_order(self, time_begin, time_end,
                          sele, loc_01, loc_02, loc_03, loc_04):
        log.info("正在执行TPshop后台系统，订单查询测试用例！")
        # 切换iframe
        self.base_iframe_switch_to(page.order_iframe)
        self.page_input_time_begin(time_begin)
        self.page_input_time_end(time_end)
        self.page_select_pay_satus(sele, loc_01)
        self.page_select_pay_code(sele, loc_02)
        self.page_select_shipping_status(sele, loc_03)
        self.page_select_order_status(sele, loc_04)
        self.page_click_search_btn()
        sleep(1)
        # 回到默认
        self.base_iframe_default()
