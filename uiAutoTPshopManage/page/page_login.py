import page
from base.base_page import BasePage
from tools.get_log import GetLogging

log = GetLogging.get_logger()


class PageLogin(BasePage):

    def input_username(self, username):
        self.base_input(page.username, username)

    def input_password(self, pwd):
        self.base_input(page.pwd, pwd)

    def input_verify_code(self, code):
        self.base_input(page.code, code)

    def click_login_btn(self):
        self.base_click(page.login_btn)

    def get_error_text(self):
        return self.base_text(page.error_text)

    # 组装登录业务
    def login(self, username, pwd, code):
        self.input_username(username)
        self.input_password(pwd)
        self.input_verify_code(code)
        self.click_login_btn()

    # 登录依赖使用
    def login_success(self, username="admin", pwd="admin@123", code=8888):
        log.info("正在进行TPshop后台系统登录！用户名:%s 密码:%s 验证码:%d" % (username, pwd, code))
        self.input_username(username)
        self.input_password(pwd)
        self.input_verify_code(code)
        self.click_login_btn()
