import unittest
from parameterized import parameterized
from base.base_page import BasePage
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLogging
from tools.read_login_json import get_data

log = GetLogging.get_logger()


class TestLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver.get_driver()
        page_in = PageIn(cls.driver)
        cls.page_in_login = page_in.page_get_PageLogin()
        cls.page_in_index = page_in.page_get_PageIndex()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, expect_result, success):
        self.page_in_login.login(username, pwd, code)

        if success:
            try:
                self.assertIn(expect_result, self.page_in_index.page_get_admin_text())
            except AssertionError as e:
                log.error("断言错误，错误信息：%s" % e)
                BasePage.base_get_img(self.driver)
                raise
        else:
            msg = self.page_in_login.get_error_text()
            try:
                self.assertEqual(expect_result, msg)
            except AssertionError as e:
                log.error("断言错误，错误信息：%s" % e)
                BasePage.base_get_img(self.driver)
                raise
