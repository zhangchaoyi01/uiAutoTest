from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

import page
from base.base_page import BasePage
from page.page_in import PageIn

driver = webdriver.Chrome()
driver.get("http://www.tpshop.com/index.php/Admin/Index/index")

page_in_login = PageIn(driver).page_get_PageLogin()
page_in_index = PageIn(driver).page_get_PageIndex()
page_in_shop = PageIn(driver).page_get_PageShop()
base_page = BasePage(driver)
page_in_login.login_success()
page_in_index.page_click_shop_btn()
page_in_shop.page_click_order()


def base_find(loc, timeout=15, poll=0.5):
    # 显示等待+定位元素
    return WebDriverWait(driver,
                         timeout=timeout,
                         poll_frequency=poll).until(lambda x: x.find_element(*loc))


base_page.base_iframe_switch_to(page.order_iframe)
el = driver.find_element(By.XPATH, "//*[@id='search-form2']/div/div[3]/select")

select = Select(el)


def base_select_find(sele, location):
    if sele == "text":
        select.select_by_visible_text(location)
    elif sele == "value":
        select.select_by_value(location)
    elif sele == "index":
        select.select_by_index(location)


base_select_find("text", "未支付")
