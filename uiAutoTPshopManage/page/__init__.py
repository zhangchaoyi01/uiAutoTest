from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""
CSS定位方法：效率高（能用CSS不用XPATH）
    ID：#username

    class选择器：如：.telA <选择class属性值为telA的所有元素>  根据元素class属性来选择

    元素选择器：如：input <选择所有input元素>  根据元素的标签名选择

    层级选择器：如：p>input <返回所有p元素下所有的input元素>  格式：element>element 
              说明：根据元素的父子关系来选择   
              提示：> 可以用空格代替 如：p input 或者 p [type='password']

    属性选择器：格式：[attribute=value] 如：[type="password"] <选择所有type属性值为password的值>
              说明：根据元素的属性名和值来选择

    1. input[type^='p']     说明：type属性以p字母开头的元素
    2. input[type$='d']     说明：type属性以d字母结束的元素
    3. input[type*='w']     说明：type属性包含w字母的元素
"""

# TPshop后台地址
url_back = "http://www.tpshop.com/index.php/Admin/Admin/login"

"""-----------------------------------------page_login_element------------------------------------------"""

username = (By.NAME, "username")
pwd = (By.NAME, "password")
code = (By.NAME, "vertify")
login_btn = (By.XPATH, "//span/input[@value='登录']")
error_text = (By.ID, "error")

"""-----------------------------------------page_index_element------------------------------------------"""

shop_btn = (By.XPATH, "//a[text()='商城']")
admin_text = (By.CSS_SELECTOR, ".manager")

"""-----------------------------------------page_shop_element------------------------------------------"""

# 订单按钮
order_btn = (By.CSS_SELECTOR, ".ico-shop-1")
# iframe
order_iframe = (By.CSS_SELECTOR, "#workspace")
# 下单开始时间
time_begin = (By.CSS_SELECTOR, "[placeholder='下单开始时间']")
# 下单结束时间
time_end = (By.CSS_SELECTOR, "[placeholder='下单结束时间']")
# 支付状态
pay_status = By.NAME, "pay_status"
# 支付方式
pay_code = By.NAME, "pay_code"
# 发货状态
shipping_status = By.NAME, "shipping_status"
# 订单状态
order_status = By.NAME, "order_status"
# 搜索按钮
search_btn = By.CSS_SELECTOR, "[value='搜索']"
# 没有符合条件的记录
no_data = By.CSS_SELECTOR, ".no-data"
# 刷新数据
refresh = By.XPATH, "//*[@class='fa fa-refresh']"
