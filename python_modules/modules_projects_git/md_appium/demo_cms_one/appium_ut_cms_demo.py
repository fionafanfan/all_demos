#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/27 16:43
# @File     : appium_ut_cms_demo.py
# @Desc     :

"""
appium
"""
import time
import unittest
from collections import namedtuple
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException, UnexpectedAlertPresentException,
                                        ElementNotInteractableException, ElementClickInterceptedException,
                                        NoAlertPresentException, InvalidElementStateException,
                                        StaleElementReferenceException, WebDriverException)

from messages import LoginRequestMsg
from messages import ServerEventIdType


capabilities = {
  "platformName": "Android",
  "automationName": "uiautomator2",
  "appium.options": {
    "automationName": "uiautomator2",
    "deviceName": "192.168.0.151:5555",
    "noRes": True,
    "disableWindowAnimation": True,
    "skipDeviceInitialization": True,
    "autoGrantPermissions": True,
    "suppressKillServer": True,
    "hideKeyboard": True,
    "noSign": True,
    "skipUnlock": True,
    "unlockStrategy": "uiautomator2"
  },
  "appPackage": "com.cmschina.cmschina_hk_app",
  "appActivity": "com.cmschina.cmschina_hk_app.MainActivity",
  "appium.settings": {
    "ignoreUnimportantViews": True,
    "allowInvisibleElements": True
  },
  "noReset": True
}


appium_server_url = 'http://localhost:4723'


class Index(object):
    my = 'descriptionStartsWith("我的").index(4)'


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


class _MyWebDriverWait(WebDriverWait):
    """
    继承WebDriverWait类，可以初始化后设置超时参数
    """
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout


_IMPLICIT_WAIT_TIME = 10 # 全局隐式等待时间
_EXPLICIT_WAIT_TIME = 3 # 全局显示等待时间

# 元素定位信息
ElementSelect = namedtuple('ElementSelector', [
    # 名称、定位方法(By.XPATH、By.CSS_SELECTOR)、选择表达式、期望状态
    # 期望状态: clickable、visible、located、text(内容不为空)
    'name', 'method', 'selector', 'status'
])

ElementSelector = namedtuple('ElementSelector', [
    'name', 'method', 'selector', 'status'
])


class CmsBot(object):
    """
    招商国际app版本
    """
    def __init__(self):
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self._wait: _MyWebDriverWait = None
        self._wait = _MyWebDriverWait(self.driver, _EXPLICIT_WAIT_TIME, ignored_exceptions=(NoSuchElementException,
                                                                                            KeyboardInterrupt))
        self.login_parameter = LoginRequestMsg()

    def is_element_clickable(self, method=By.CSS_SELECTOR, xpath_or_css_str='',
                             wait_time=_EXPLICIT_WAIT_TIME):
        """
        界面元素在等待的时间内是否可点击
        """
        located = True
        self.driver.implicitly_wait(wait_time)
        self._wait.timeout = wait_time

        try:
            self._wait.until(EC.element_to_be_clickable((method, xpath_or_css_str)))
        except TimeoutException:
            located = False

        self.driver.implicitly_wait(_IMPLICIT_WAIT_TIME)
        self._wait.timeout = _EXPLICIT_WAIT_TIME

        return located

    def is_element_visible(self, method=By.CSS_SELECTOR, xpath_or_css_str='',
                           wait_time=_EXPLICIT_WAIT_TIME):
        """
        界面元素在等待的时间内是否已经可见
        """
        located = True
        self.driver.implicitly_wait(wait_time)
        self._wait.timeout = wait_time

        try:
            self._wait.until(EC.visibility_of_element_located((method, xpath_or_css_str)))
        except TimeoutException:
            located = False

        self.driver.implicitly_wait(_IMPLICIT_WAIT_TIME)
        self._wait.timeout = _EXPLICIT_WAIT_TIME

        return located

    def is_element_located(self, method=By.CSS_SELECTOR, xpath_or_css_str='',
                           wait_time=_EXPLICIT_WAIT_TIME):
        """
        界面元素在等待的时间内是否已经加载
        """
        located = True
        self.driver.implicitly_wait(wait_time)
        self._wait.timeout = wait_time

        try:
            self._wait.until(EC.presence_of_element_located((method, xpath_or_css_str)))
        except TimeoutException:
            located = False

        self.driver.implicitly_wait(_IMPLICIT_WAIT_TIME)
        self._wait.timeout = _EXPLICIT_WAIT_TIME

        return located

    def select_element(self, element_selects: [ElementSelect], wait_time=10):
        """
        选择元素
        """
        max_wait_time = time.time() + wait_time
        name = ''
        element_selects = [element_selects] if not isinstance(element_selects, list) else element_selects
        while not name and time.time() < max_wait_time:
            for element_select in element_selects:
                if element_select.status == 'clickable':
                    check_func = self.is_element_clickable
                elif element_select.status == 'visible':
                    check_func = self.is_element_visible
                elif element_select.status == 'located':
                    check_func = self.is_element_located
                elif element_select.status == 'text':
                    if not self.is_element_visible(element_select.method, element_select.selector, wait_time=0.5):
                        continue
                    check_func = self.driver.find_element
                    if len(check_func(element_select.method, element_select.selector).text) > 0:
                        name = element_select.name
                        break
                    continue
                else:
                    continue
                if check_func(element_select.method, element_select.selector, wait_time=0.5):
                    name = element_select.name
                    break
        return name

    def on_login(self):
        """
        登录请求
        :return:
        """
        if self.login_parameter.serverEventId == ServerEventIdType.StartConn:
            self.login_start_conn()
        elif self.login_parameter.serverEventId == ServerEventIdType.SendAcctPwd:
            self.login_with_account()

    def check_login_start(self):
        """
        判断启动连接成功还是失败
        如果当前处于-我的 界面，则认为启动连接成功
        :return:
        """
        my_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Index.my)
        page_status = self.select_element([ElementSelector(name='my', method=AppiumBy.ANDROID_UIAUTOMATOR,
                                                           selector=Index.my,
                                                           status='clickable')

                                           ])
        if page_status == 'my':
            return True
        else:
            return False

    def check_login_start_page(self):
        """
        确认是否已完成前置操作，处于可以进行交易登录条件
        :return:
        """
        page_status = self.select_element([ElementSelector(name='login_phone', method=AppiumBy.ANDROID_UIAUTOMATOR,
                                                           selector=Login.login_phone_button,
                                                           status='clickable')

                                           ])
        if page_status == 'login_phone':
            return False
        else:
            return True

    def check_page_name(self):
        """
        判断页面状态
        :return:
        """
        pass

    def login_start_conn(self):
        """
        启动连接:
        13-启动连接成功: 返回启动连接成功信息，同时去检测当前是否已完成前置动作。
        14-启动连接失败： 结束流程
        :return:
        """
        is_start_success = self.check_login_start()
        if is_start_success:
            print("启动成功")
            is_ready_login = self.check_login_start_page()
            if is_ready_login:
                print("前置操作已完成， 可以进行后续的账号密码登录动作")
            else:
                print("招商国际app未完成注册，请在手机端完成注册后，再次启动机器手连接")
        else:
            print("启动失败")

    def login_with_account(self):
        """
        请求登录， 输入账号密码
        :return:
        """
        page_name = self.check_page_name()
        if page_name == 'login':
            print("已登录")
        elif page_name == 'logout':
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

    def clear(self):
        if self.driver:
            self.driver.quit()


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = CmsBot()

    def tearDown(self) -> None:
        self.bot.clear()

    # @unittest.skip('')
    # def test_find_battery(self):
    #     el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[text="Battery"]')
    #     el.click()

    # def test_find_capture_input(self):
    #     el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'textContains("请输入图形验证码")')
    #     print('test_find_capture_input>>', el)

    # def test_find_capture_error(self):
    #     """
    #     模拟输入图形验证码错误，抓取错误文案
    #     :return:
    #     """
    #     el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'textContains("请输入图形验证码")')
    #     el.send_keys('2185')
    #     el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'descriptionContains("确 定")')
    #     el.click()
    #     print("submit capture")
    #     capture_error_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'descriptionContains("图形验证码错误")')
    #     print('capture_error_el>>', capture_error_el)
    #     capture_time_error_much_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'descriptionContains("验证码错误次数过多")')
    #     print('capture_time_error_much_el>>', capture_time_error_much_el)

    @unittest.skip('')
    def test_input(self):
        pass
        # self.driver.find_element(AppiumBy.ID,'com.wetrade.financial:id/etUserName').send_keys('test')

    def test_login_start_conn(self):
        self.bot.login_start_conn()


if __name__ == '__main__':
    unittest.main()


