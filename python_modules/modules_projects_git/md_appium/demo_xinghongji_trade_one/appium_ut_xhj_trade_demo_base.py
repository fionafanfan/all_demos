#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/20 17:16
# @File     : appium_ut_xhj_demo.py
# @Desc     :

"""
appium
"""
import enum
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

"""
{
  "platformName": "Android",
  "appium:udid": "R5CNA0C587T",
  "automationName": "uiautomator2",
  "appium.options": {
    "automationName": "uiautomator2",
    "deviceName": "R5CNA0C587T",
    "noRes": true,
    "disableWindowAnimation": true,
    "skipDeviceInitialization": true,
    "autoGrantPermissions": true,
    "suppressKillServer": true,
    "hideKeyboard": true,
    "noSign": true,
    "skipUnlock": true,
    "unlockStrategy": "uiautomator2"
  },
  "appPackage": "com.gt.shk",
  "appActivity": "com.gt.shk.MainActivity ",
  "appium.settings": {
    "ignoreUnimportantViews": true,
    "allowInvisibleElements": true
  },
  "noReset": true
}
"""

capabilities = {
  "platformName": "Android",
  "appium:udid": "R5CNA0C587T",
  "automationName": "uiautomator2",
  "appium.options": {
    "automationName": "uiautomator2",
    "deviceName": "R5CNA0C587T",
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
  "appPackage": "com.gt.shk",
  "appActivity": "com.gt.shk.MainActivity ",
  "appium.settings": {
    "ignoreUnimportantViews": True,
    "allowInvisibleElements": True
  },
  "noReset": True
}


appium_server_url = 'http://localhost:4723'

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


_IMPLICIT_WAIT_TIME = 10  # 全局隐式等待时间
_EXPLICIT_WAIT_TIME = 3  # 全局显示等待时间

# 元素定位信息
ElementSelect = namedtuple('ElementSelector', [
    # 名称、定位方法(By.XPATH、By.CSS_SELECTOR)、选择表达式、期望状态
    # 期望状态: clickable、visible、located、text(内容不为空)
    'name', 'method', 'selector', 'status'
])

ElementSelector = namedtuple('ElementSelector', [
    'name', 'method', 'selector', 'status'
])


class PageElem(object):
    """
    页面元素定位
    """
    login_user = '//android.widget.EditText[@resource-id="com.gt.shk:id/et_login_id"]'
    login_pwd = '//android.widget.EditText[@resource-id="com.gt.shk:id/et_login_pwd"]'
    login_submit = '//android.widget.TextView[@resource-id="com.gt.shk:id/tv_login_btn"]'

    login_otp_page = '//android.widget.TextView[@resource-id="com.gt.shk:id/tv_please_enter_your_one_time_login_security_code"]'
    login_otp_page2 = '//android.widget.TextView[@resource-id="com.gt.shk:id/tv_title" and @text="登入安全编码"]'
    login_otp_submit = '//android.widget.TextView[@resource-id="com.gt.shk:id/btn_submit"]'

    login_otp_error = '//android.widget.TextView[@resource-id="android:id/message" and @text="请输入您的一次性密码"]'


class XhjTradeBot(object):
    """
    新鸿基app版本
    """
    @enum.unique
    class Page(enum.Flag):
        """
        页面
        """
        Login = enum.auto()  # 登录
        LoginSuccess = enum.auto()  # 登录成功
        Order = enum.auto()  # 交易
        Online = enum.auto()  # 在线判断

    def __init__(self):
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self._wait: _MyWebDriverWait = None
        self._wait = _MyWebDriverWait(self.driver, _EXPLICIT_WAIT_TIME, ignored_exceptions=(NoSuchElementException,
                                                                                            KeyboardInterrupt))
        self.pkg_name = capabilities.get('appPackage', '')

    def clear(self):
        if self.driver:
            self.driver.quit()


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = XhjTradeBot()

    def tearDown(self) -> None:
        self.bot.clear()

    def test_login_with_account(self):
        login_user_el = self.bot.driver.find_element(AppiumBy.XPATH, PageElem.login_user)
        login_user_el.click()
        login_user_el.clear()
        login_user_el.send_keys('user')
        login_pwd_el = self.bot.driver.find_element(AppiumBy.XPATH, PageElem.login_pwd)
        login_pwd_el.click()
        login_pwd_el.clear()
        login_pwd_el.send_keys('pwd')
        login_submit = self.bot.driver.find_element(AppiumBy.XPATH, PageElem.login_submit)
        login_submit.click()
        print('输入完账号密码')

    def test_login_with_account_resp(self):
        """
        输入账号返回
        :return:
        """
        login_account_error = '//android.widget.TextView[@resource-id="android:id/message" and @text="您输入的登入名称或密码错误，请再次登入。"]'
        login_account_error_el = self.bot.driver.find_element(AppiumBy.XPATH, login_account_error)
        if login_account_error_el:
            print('您输入的登入名称或密码错误，请再次登入。')

    def test_login_with_otp(self):
        """登录用otp
           send_keys这个方法可行, 但是好像有点慢， 因为要一个一个输入， 需要6次io。
        """
        otp_page_el = self.bot.driver.find_element(AppiumBy.XPATH, PageElem.login_otp_page)
        if otp_page_el:
            print("当前为输入保安编码页-判断1")

        otp_page_el2 = self.bot.driver.find_element(AppiumBy.XPATH, PageElem.login_otp_page2)
        if otp_page_el2:
            print("当前为输入保安编码页-判断2")

        login_otp_input_temp = '//android.widget.TextView[@resource-id="com.gt.shk:id/ET_PIN_NUM"]'
        otp_str = '234119'
        for i, s in enumerate(otp_str):
            login_otp_input = login_otp_input_temp.replace('ET_PIN_NUM', f'et_pin_num{i+1}')
            el = self.bot.driver.find_element(AppiumBy.XPATH, login_otp_input)
            el.click()
            el.clear()
            el.send_keys(s)
        print('发送otp')
        # 需要隐藏键盘，才能找到提交按钮

        login_otp_submit = self.bot.driver.find_element(AppiumBy.XPATH, PageElem.login_otp_submit)
        login_otp_submit.click()
        print('提交otp成功')

    def test_login_with_otp_resp(self):
        login_otp_error = self.bot.driver.find_element(AppiumBy.XPATH, PageElem.login_otp_error)
        if login_otp_error:
            print('请输入您的一次性密码')
        button = '//android.widget.Button[@resource-id="android:id/button3"]'
        self.bot.driver.find_element(AppiumBy.XPATH, button).click()
        self.bot.driver.back()  # 不能回退弹框, 但是有的页面间跳转可以。

    def test_login_with_account_resp(self):
        pass

    @unittest.skip('')
    def test_press_keycode(self):
        """
        测试按键盘
        :return:
        """

        from appium.webdriver.extensions.android.nativekey import AndroidKey
        key_num_map = {0: AndroidKey.DIGIT_0,
                       1: AndroidKey.DIGIT_1,
                       2: AndroidKey.DIGIT_2,
                       3: AndroidKey.DIGIT_3,
                       4: AndroidKey.DIGIT_4,
                       5: AndroidKey.DIGIT_5,
                       6: AndroidKey.DIGIT_6,
                       7: AndroidKey.DIGIT_7,
                       8: AndroidKey.DIGIT_8,
                       9: AndroidKey.DIGIT_9,
                       }
        # # 清除旧的输入
        for i in range(6):
            self.bot.driver.press_keycode(AndroidKey.DEL)
        opt = '794161'
        for i in opt:
            # 模拟键盘输入验证码 "1234"
            self.bot.driver.press_keycode(key_num_map[int(i)])

        otp_check_el = self.bot.driver.find_element(Login.otp_check)
        otp_check_el.click()
        # opt = '123456'
        # for i in opt:
        #     # 模拟键盘输入验证码 "1234"
        #     self.bot.driver.press_keycode(key_num_map[int(i)])
        # self.bot.driver.press_keycode(AndroidKey.CLEAR)  # 不起作用
        # self.bot.driver.press_keycode(AndroidKey.PAGE_DOWN)


if __name__ == '__main__':
    unittest.main()


