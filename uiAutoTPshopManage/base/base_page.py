import sys
from selenium.webdriver.support.wait import WebDriverWait
import config
from selenium.webdriver.support.select import Select
from tools.get_log import GetLogging

log = GetLogging.get_logger()


class BasePage:

    def __init__(self, driver):
        log.info("正在初始化driver!")
        self.driver = driver

    def base_find(self, loc, timeout=30, poll=0.5):
        # 显示等待+定位元素
        log.info("正在定位元素[%s:%s]" % (loc[0], loc[1]))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_select_find(self, loc, sele, location):
        # 初始化select定位方法
        select = Select(self.base_find(loc))
        log.info("正在选择下拉框：[%s:%s]" % (sele, location))
        if sele == "text":
            select.select_by_visible_text(location)
        elif sele == "value":
            select.select_by_value(location)
        elif sele == "index":
            select.select_by_index(location)

    def base_input(self, loc, value):
        el = self.base_find(loc)
        log.info("正在对[%s:%s]输入框进行清空" % (loc[0], loc[1]))
        el.clear()
        log.info("正在对[%s:%s]输入框输入内容：%s" % (loc[0], loc[1], value))
        el.send_keys(value)

    def base_click(self, loc):
        log.info("正在点击[%s:%s]元素" % (loc[0], loc[1]))
        self.base_find(loc).click()

    def base_text(self, loc):
        text = self.base_find(loc).text
        log.info("正在获取%s元素文本：%s" % (loc, text))
        return text

    def base_iframe_switch_to(self, iframe):
        order_iframe = self.base_find(iframe)
        log.info("正在切换iframe表单：%s" % order_iframe)
        self.driver.switch_to.frame(order_iframe)

    def base_iframe_default(self):
        log.info("返回到默认表单!")
        self.driver.switch_to.default_content()

    @staticmethod
    def base_get_img(driver):
        log.info("断言错误，正在进行截图操作!")
        driver.get_screenshot_as_file(
            config.file_path("image") + "%s.png" % config.new_time)
