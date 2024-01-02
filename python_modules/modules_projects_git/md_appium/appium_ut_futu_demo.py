"""
appium
"""
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


capabilities = {
  "platformName": "Android",
  "appium:automationName": "uiautomator2",
  "appium:appium.options": {
    "automationName": "uiautomator2",
    "deviceName": "192.168.0.172:5555",
    "noRes": True
  },
  "appium:appPackage": "cn.futu.trader",
  "appium:appActivity": "cn.futu.trader.launch.activity.LaunchActivity",
  "appium:appium.settings": {
    "ignoreUnimportantViews": True,
    "allowInvisibleElements": True
  },
  "appium:noReset": False
}


appium_server_url = 'http://localhost:4723'


class Login(object):
    """
    登录流程：
    1、未完成前置操作， 提醒完成前置操作
    2. 已完成前置操作，

    考虑错误场景提示
    1. 账号密码输入错误
    2. 图形验证码输入错误、看不清刷新验证码、超时
    3. otp输入错误， 输入错误次数、超时

    图形验证码输入错误次数过多，会被不限制锁住1小时  (验证码错误次数过多，锁定21分钟)
    交易验证码opt, 发送到短信，验证码5分钟内有效， 页面重发需等待60s，才能重新发送验证码
    """
    login_phone_button = 'descriptionStartsWith("登录/注册")'  # 手机号登录注册
    login_button = 'descriptionContains("我的账户").descriptionContains("登录")'  # 登录触发按钮元素
    after_login = 'descriptionContains("我的账户").descriptionContains("已登录")'  # 已登录

    login_page_title = 'descriptionContains("交易登录").index(1)'  # 交易登录页的标题
    login_user = f'//android.view.View[@content-desc="account"]'  # 交易账户-如果进入交易登录页，账号是固定的;
    # 传入账号进行比对88811489， 如果找得到，则代表账号输入正确
    login_passwd = '//android.widget.EditText[@text="请输入登录密码"]'  # 交易账户-密码; xpath locator
    read_agreement = 'descriptionContains("已阅读并同意")'  # 已阅读协议, self.driver.tap([tuple(e.location_in_view.values())])
    login_submit = 'descriptionContains("交易登录").index(7)'  # 交易登录请求提交

    # 登录图形验证码-(前置动作 和 首次完成手机号登录，再输入密码登录 都有, 但只需要考虑后者，元素定位都是一样的)
    image_capture = '//android.widget.ImageView[@content-desc="看不清？点击换一个"]'  # 图形验证码图片
    image_capture_update = '//android.widget.ImageView[@content-desc="看不清？点击换一个"]'  # 刷新图形验证码
    image_capture_input = 'textContains("请输入图形验证码")'  # 请输入图形验证码
    image_capture_input_check = 'descriptionContains("确 定")'  # 输入图形验证码确认
    capture_error = '//android.view.View[@content-desc="验证码错误次数过多"]/android.view.View/android.view.View'

    # 交易验证码opt
    otp_input = '//android.view.View[3]'  # otp输入
    otp_check = 'descriptionContains("确 定")'  # otp提交


class Logout(object):
    """
    登出流程
    """
    logout_button = 'descriptionContains("账户设置").descriptionContains("退出登录")'  # 退出登录按钮
    check_logout_yes_button = 'descriptionContains("确认退出")'  # 确认是否要退出
    check_logout_cancel_button = 'descriptionContains("取消")'  # 取消退出
    check_logout_content = 'descriptionContains("退出后，您将无法交易或查看持仓信息，请确认是否需要退出")'


class MyAppium(object):
    pass


class CmsBot(object):
    """
    招商国际app版本
    """
    def login(self):
        """
        登录
        :return:
        """
        pass

    def logout(self):
        """
        登出
        :return:
        """
        pass

    def check_page(self):
        """确认当前是哪个页面"""
        pass


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    @unittest.skip('')
    def test_find_battery(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[text="Battery"]')
        el.click()

    def test_find_capture_error(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="验证码错误次数过多"]/android.view.View/android.view.View')
        print(el)

    def test_input(self):
        pass
        # self.driver.find_element(AppiumBy.ID,'com.wetrade.financial:id/etUserName').send_keys('test')

    def test_login(self):
        pass

    def test_logout(self):
        pass

    def test_check_page(self):
        pass


if __name__ == '__main__':
    unittest.main()

