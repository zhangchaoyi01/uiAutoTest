import unittest
import config
from scripts.test_login import TestLogin
from scripts.test_order_search import TestOrderSearch
from tools.HTMLTestReportCN import HTMLTestRunner
from tools.get_log import GetLogging


if __name__ == '__main__':
    # Initialize the test suite
    suite = unittest.TestSuite()
    # Assemble test cases
    suite.addTest(unittest.makeSuite(TestLogin))
    suite.addTest(unittest.makeSuite(TestOrderSearch))
    report_name = config.file_path("report") + config.new_time + "_report.html"
    # Write a test report
    log = GetLogging.get_logger()
    with open(report_name, "wb") as f:
        HTMLTestRunner(stream=f,
                       verbosity=2,
                       title="后台系统登录",
                       description="测试平台：windows",
                       tester="QA").run(suite)
    log.info("正在导出测试报告....")
