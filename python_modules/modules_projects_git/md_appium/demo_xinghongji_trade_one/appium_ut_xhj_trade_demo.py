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


class Index(object):
    menu_index = '//android.widget.Button[@text="首頁"]'  # 首页  虽然界面显示可点击，但实际获取元素判定却不可点击
    menu_price = '//android.widget.Button[@text="報價"]'    # 报价  可点击
    menu_trade = '//android.widget.Button[@text="股票交易"]'  # 股票交易  可点击

    go_to_account = '//android.widget.ImageButton[@resource-id="com.firstsechk.tc.trade:id/btn_Account"]'  # 首页左上角按钮


class Account(object):
    account_title = '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lbl_Title" and @text="環球投資理財一站式服務"]'
    ready_account = '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lbl_Value" and @text="證券賬戶"]'  #  如果在线，跳出账号弹框
    open_account = '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lbl_Cap" and @text="綁定 / 開設賬戶"]'  # 如果不在线，跳转到登录页， 如果在线，这个元素也找不到


class Position(object):
    position = '//android.widget.Button[@resource-id="com.firstsechk.tc.trade:id/btnPosition"]'  # 持仓按钮


class LogoutExp(object):
    relogout  = '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lblVal_Message" and @text="重複登錄!"]'  # 重复登录，被挤掉线
    relogout_check = '//android.widget.LinearLayout[@resource-id="com.firstsechk.tc.trade:id/view_Button"]'


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
    # 第一证券
    login_user = '//android.widget.EditText[@resource-id="com.firstsechk.tc.trade:id/txt_EditID"]'  # 输入账号;
    login_passwd = '//android.widget.EditText[@resource-id="com.firstsechk.tc.trade:id/txt_EditPwd"]'  # 输入密码
    login_button = '//android.widget.Button[@resource-id="com.firstsechk.tc.trade:id/btn_Login"]'  # 登录触发按钮元素

    passwd_error = '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lblVal_Message" and @text="密碼錯誤 (SEW002)"]'
    passwd_error_check = '//android.widget.Button[@resource-id="com.firstsechk.tc.trade:id/btn_Positive" and @text="確定"]'  # 密码错误弹框取消
    after_login = 'descriptionContains("我的账户").descriptionContains("已登录")'  # 已登录
    error_connect = '//android.widget.TextView[@text="你的連接已無效"]'  # √
    error_connect_check = '//android.widget.Button[@text="你的連接已無效"]'

    error_no_quanxian = '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lblVal_Title" and @text="没有權限"]'  # 没有权限弹框, 会过一会自己消失掉
    # 第一证券
    # 输入账号密码失败
    login_error = '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lblVal_Title" and @text="證券賬戶 - 登入失敗"]'

    # 交易验证码opt
    otp_title = 'descriptionContains("交易验证")'  # 交易验证otp页面标识
    otp_input = '//android.view.View[contains(@content-desc, "已发送验证码至")]/following-sibling::android.view.View' # otp输入
    otp_input_old = '//android.view.View[3]'  # otp输入
    otp_check = 'descriptionContains("确 定")'  # otp提交
    otp_refresh = 'descriptionContains("重新发送")'  # otp重新获取


class Logout(object):
    """
    登出流程
    """
    account_settings = 'descriptionContains("账户设置")'  # 账户设置
    logout_button = 'descriptionContains("账户设置").descriptionContains("退出登录")'  # 退出登录按钮
    check_logout_yes_button = 'descriptionContains("确认退出")'  # 确认是否要退出
    check_logout_cancel_button = 'descriptionContains("取消")'  # 取消退出
    check_logout_content = 'descriptionContains("退出后，您将无法交易或查看持仓信息，请确认是否需要退出")'

    disconnect = '//android.view.View[@content-desc="系统连接中断"]'  # 掉线通知（被挤下线）
    disconnect_know = '//android.view.View[@content-desc="我知道了"]'  # 掉线通知确认接收



class PageElem(object):
    """
    页面元素定位
    """
    pass


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
        self.login_parameter = LoginRequestMsg()
        self.pkg_name = capabilities.get('appPackage', '')

    def is_login(self):
        """
        Todo: 判断页面是否登录成功在线
        :return:
        """
        return self.is_in_page(self.Page.Online)

    def on_loop(self):
        """
        Todo: 主循环
        :return:
        """
        pass

    def is_in_page(self):
        """
        Todo: 是否已处于某个页面
        :return:
        """
        pass

    def keep_login(self):
        """
        Todo: 保持登录
        :return:
        """
        pass

    def get_app_state(self):
        app_status_map = {
            1: "应用没有在运行，已关闭状态",
            3: "应用在后台运行",
            4: "应用在前台运行"
        }
        pkg_state = self.driver.query_app_state(self.pkg_name)
        print(app_status_map.get(pkg_state, ''))

    def get_network_connection(self):
        network_status = self.driver.network_connection
        print("网络状态:", network_status)
        if network_status == 0:  # 0 表示无网络连接
            print("网络连接断开，用户可能已掉线")
        else:
            print("网络连接正常")  # 网络状态: 6

    def login_first_pro(self):
        pass

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

    def my_select_element(self, element_selects: [ElementSelect], wait_time=10):
        max_wait_time = time.time() + wait_time
        name = ''
        element_selects = [element_selects] if not isinstance(element_selects, list) else element_selects
        while not name and time.time() < max_wait_time:
            check = False
            for element_select in element_selects:
                try:
                    el = self.driver.find_element(element_select.method, element_select.selector)

                    if element_select.status == 'clickable':
                        check = el.get_attribute('clickable')
                    elif element_select.status == 'display':
                        check = el.get_attribute('displayed')
                    elif element_select.status == 'located':
                        check = el
                    elif element_select.status == 'text':
                        check = el.get_attribute('content-desc')
                    else:
                        continue
                except Exception as e:
                    print("未找到相应的元素", e)

                finally:
                    if check:
                        return element_select.name
        return name

    def select_multi_elements_old(self, all_name_elements):
        """
        多个元素组合判定指定页面
        :return:
        """
        name = ""
        for name_elements in all_name_elements:
            name, elements = name_elements[0], name_elements[1]
            els_name = [e['name'] for e in elements]
            for elem in elements:
                el = self.my_select_element([ElementSelector(name=elem['name'], method=elem['method'],
                                selector=elem['selector'],
                                status=elem['status'])], wait_time=1)
                if el not in els_name:
                    name = ""  # 重置为无
                    break
        return name

    def select_multi_elements(self, all_name_elements):
        """
        多个元素组合判定指定页面
        :return:
        """
        name = ""
        for name_elements in all_name_elements:
            name, elements = name_elements[0], name_elements[1]
            els_name = [e['name'] for e in elements]
            for elem in elements:
                el = self.select_element([ElementSelector(name=elem['name'], method=elem['method'],
                                selector=elem['selector'],
                                status=elem['status'])], wait_time=1)
                if el not in els_name:
                    name = ""  # 重置为无
                    break
        return name

    @staticmethod
    def get_element_part_position(e: webdriver.webelement.WebElement, part='front_center'):
        """
        获取元素部分位置
        :param e:
        :param part:
        :return part: 位置坐标
        """
        if part == 'front_center':
            x = e.location_in_view['x'] + e.size['width'] / 4
            y = e.location_in_view['y'] + e.size['height'] / 2
        elif part == 'back_center':
            x = e.location_in_view['x'] + e.size['width'] / 4 * 3
            y = e.location_in_view['y'] + e.size['height'] / 2
        else:
            x = y = -1

        return int(x), int(y)

    def on_login(self):
        """
        登录请求
        :return:
        """
        if self.login_parameter.serverEventId == ServerEventIdType.StartConn:
            self.login_start_conn()
        elif self.login_parameter.serverEventId == ServerEventIdType.SendAcctPwd:
            self.login_with_account()
        elif self.login_parameter.serverEventId == ServerEventIdType.SendImgVerification:
            self.login_with_img_capture()
        elif self.login_parameter.serverEventId == ServerEventIdType.RefreshImgVerification:
            self.refresh_img_capture()
        elif self.login_parameter.serverEventId == ServerEventIdType.SendOtp:
            self.login_with_otp()
        elif self.login_parameter.serverEventId == ServerEventIdType.RefreshOtp:
            self.resend_otp()

    def logout(self):
        """
        手动退出登录:
        1、回到首页
        2、进入-我的 页面
        2、进入 账户设置 页面
        3、点击 退出登录
        4、点击 确认退出

        ret:
        退出登录成功
        退出登录失败
        :return:
        """
        self.back_index_page()  # 返回首页
        my_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Index.my)
        my_el.click()
        time.sleep(1)
        account_settings_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Logout.account_settings)
        account_settings_el.click()
        time.sleep(1)
        logout_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Logout.logout_button)
        logout_el.click()
        check_logout_yes_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Logout.check_logout_yes_button)
        check_logout_yes_el.click()
        print("已退出登录")

    def logout2(self):
        """
        退出的第二种方式
        :return:
        """
        app_id = self.driver.current_package
        print("appid", app_id)

    def check_index_page(self):
        """
        判断启动连接成功还是失败
        如果当前处于-我的 界面，则认为启动连接成功
        :return:
        """

        login_start_page_selector = [
            {
                "name": "my_click",
                "method": AppiumBy.ANDROID_UIAUTOMATOR,
                "selector": Index.my,
                "status": "clickable"
            }
        ]

        page_selector = [("my", login_start_page_selector)]
        page = self.select_multi_elements(page_selector)
        return page

    def check_page_name(self, name=""):
        """
        判断页面状态
        : name : 如果有具体，则判断特定页面即可
        :return:
        """
        register_page_selector = [
            {
                "name": "login_phone",
                "method": AppiumBy.ANDROID_UIAUTOMATOR,
                "selector": Login.login_phone_button,
                "status": "clickable"
            }
        ]

        ready_login_page_selector = [
                      {
                        "name": "login_my_account",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Login.login_my_account,
                        "status": "visible"
                      },
                      {
                        "name": "login_button",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Login.login_button,
                        "status": "clickable"
                      }
                    ]

        trade_login_page_page_selector = [
                      {
                        "name": "login_page_title",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Login.login_page_title,
                        "status": "visible"
                      }

                    ]

        my_page_page_selector = [
                      {
                        "name": "my_activity",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": 'descriptionContains("活动中心")',
                        "status": "visible"
                      },
                        {
                            "name": "connect_us",
                            "method": AppiumBy.ANDROID_UIAUTOMATOR,
                            "selector": 'descriptionContains("联系我们")',
                            "status": "visible"
                        }

                    ]
        page_selectors = [
                          ("register", register_page_selector),
                          ("ready_login", ready_login_page_selector),
                          ("trade_login_page", trade_login_page_page_selector),
                          ("my_page", my_page_page_selector),
                          ]
        if name:
            page_selector = [page for page in page_selectors if page[0] == name]
        else:
            page_selector = page_selectors
        page = self.select_multi_elements(page_selector)
        return page

    def check_login_page_name(self, name=""):
        """
        判断输入正确的账号后的页面状态
        : name : 如果有具体，则判断特定页面即可
        :return:
        """
        input_capture_page_selector = [
                      {
                        "name": "capture",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Login.image_capture,
                        "status": "visible"
                      }
                    ]

        login_success_page_page_selector = [
                      {
                        "name": "after_login",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Login.after_login,
                        "status": "visible"
                      },
                    {
                        "name": "my",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Index.my,
                        "status": "visible"
                    }

                    ]

        page_selectors = [("input_capture", input_capture_page_selector),
                          ("login_success", login_success_page_page_selector)
                          ]
        if name:
            page_selector = [page for page in page_selectors if page[0] == name]
        else:
            page_selector = page_selectors
        page = self.select_multi_elements(page_selector)
        return page

    def check_login_capture_page_name(self, name=""):
        """
        判断输入正确的账号后的页面状态
        : name : 如果有具体，则判断特定页面即可
        :return:
        """
        input_otp_page_selector = [
                      {
                        "name": "otp_title",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Login.otp_title,
                        "status": "visible"
                      }
                    ]

        capture_error_page_selector = [
                      {
                        "name": "capture_error",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Login.capture_error,
                        "status": "visible"
                      }
                    ]

        capture_error_lock_page_selector = [
                      {
                        "name": "capture_error_lock",
                        "method": AppiumBy.ANDROID_UIAUTOMATOR,
                        "selector": Login.capture_error_lock,
                        "status": "visible"
                      }
                    ]

        page_selectors = [("otp_input", input_otp_page_selector),
                          ("capture_error", capture_error_page_selector),
                          ("capture_error_lock", capture_error_lock_page_selector)
                          ]
        if name:
            page_selector = [page for page in page_selectors if page[0] == name]
        else:
            page_selector = page_selectors
        page = self.select_multi_elements(page_selector)
        return page

    def login_start_conn(self):
        """
        启动连接:
        13-启动连接成功: 返回启动连接成功信息。
        14-启动连接失败： 结束流程
        :return:
        """
        page_name = self.check_index_page()

        if page_name == 'my':
            my_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Index.my)
            my_el.click()
            print("启动成功")
            page_name = self.check_page_name(name="register")
            if page_name == 'register':
                print("招商国际app未完成注册，请在手机端完成注册后，再次启动机器手连接")
            else:
                print("前置操作已完成， 可以进行后续的账号密码登录动作")

        else:
            print("启动失败")

    def login_with_account(self):
        """
        请求登录， 输入账号密码
        :return:
        """
        login_user = 'user123'
        login_passwd = 'paw123'
        page_name = self.check_page_name(name='ready_login')
        if page_name == 'ready_login':
            begin_login_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Login.login_button)
            begin_login_el.click()
            time.sleep(1)  # 暂停等待
            page_name = self.check_page_name(name='trade_login_page')
            time.sleep(1)  # 暂停等待
            if page_name == 'trade_login_page':
                login_user_el = self.driver.find_element(By.XPATH, Login.login_user)
                print(f"用户账号:{login_user_el.tag_name} , {login_user_el.tag_name == login_user}")
                if login_user_el.tag_name == login_user:
                    print("账号输入正确")
                else:
                    print("账号输入错误")
                login_passwd_el = self.driver.find_element(By.XPATH, Login.login_passwd)
                login_passwd_el.click()  # 选中输入框
                login_passwd_el.clear()  # 清除原来的数据
                login_passwd_el.send_keys(login_passwd)
                read_agreement_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Login.read_agreement)
                self.driver.tap([tuple(self.get_element_part_position(read_agreement_el))])
                # 隐藏键盘， 需要设定为非安全键盘才能生效，如果是安全键盘，会无法操作
                if self.driver.is_keyboard_shown():
                    self.driver.hide_keyboard()
                login_submit_el = self.driver.find_element(By.XPATH, Login.login_submit)
                login_submit_el.click()
                print("账号密码输入成功")
                print("判断账号密码输入成功后，是跳转到图形验证码步骤还是直接登录成功步骤")
                passwd_error_el = self.driver.find_element(By.XPATH, Login.passwd_error)
                print('passwd_error_el>>', passwd_error_el)
                page_name = self.check_login_page_name()
                if page_name == 'passwd_error':
                    print("登录密码不正确")
                if page_name == 'input_capture':
                    print("需要将图形验证码返回给服务端， 并要求服务端下一步骤输入图形验证码")
                    capture_base64 = self.get_image_capture()
                    print("返回capture base64>>>", capture_base64)
                elif page_name == 'login_success':
                    print("登录成功，无需输入图形验证码及opt步骤")
                else:
                    print("未知错误")

    def login_with_img_capture(self):
        """
        输入图形验证码
        :return:
        """
        capture = '1734'
        print("服务端输入的capture", capture)
        input_capture_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Login.image_capture_input)
        input_capture_el.click()
        input_capture_el.clear()
        input_capture_el.send_keys(capture)
        image_capture_input_check_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Login.image_capture_input_check)
        image_capture_input_check_el.click()  # 确定提交图形验证码
        page_name = self.check_login_capture_page_name()
        if page_name == 'otp_input':
            print("输入otp页面")
        elif page_name == 'capture_error':
            print("图形验证码输入错误")
        elif page_name == 'capture_error_lock':
            print("验证码输入次数过多，被锁住")
        else:
            print("图形验证码输入发生未知错误")

    def login_with_otp(self):
        """
        输入otp验证码
        Todo: 发送opt无法发送
        :return:
        """
        otp = '794161'
        print("输入的otp:", otp)
        # 隐藏键盘， 需要设定为非安全键盘才能生效，如果是安全键盘，会无法操作
        if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()
        otp_input_el = self.driver.find_element(By.XPATH, Login.otp_input)
        # 使用 set_attribute 给 content-desc 赋新值

        otp_input_el.send_keys('1 \n2 \n3 \n4 \n5 \n6')

        # 获取赋值后的 content-desc 值并打印
        updated_value = otp_input_el.get_attribute("content-desc")
        print(f"Updated content-desc value: {updated_value}")
        otp_check_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Login.otp_check)
        otp_check_el.click()

    def resend_otp(self):
        """
        重新获取otp
        :return:
        """
        otp_el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Login.otp_refresh)
        otp_el.click()
        print("重新发送otp成功")

    def get_image_capture(self):
        """
        获取图形验证码
        :return:
        """
        e = self.driver.find_element(AppiumBy.XPATH, Login.image_capture)
        capture_base64 = e.screenshot_as_base64
        with open('cms_captcha.png', 'wb') as f:
            f.write(e.screenshot_as_png)
        print("capture保存成功")
        return capture_base64

    def refresh_img_capture(self):
        """
        刷新图形验证码
        :return:
        """
        pass

    def back_page(self):
        """
        返回上一页
        :return:
        """
        self.driver.back()

    def back_index_page(self):
        """
        返回到app首页， 下面主menu点击菜单的页面即可。
        :return:
        """
        while True:
            page_name = self.check_index_page()
            if page_name == 'my':
                print("当前页面为首页")
                break
            else:
                self.back_page()

    def logout_app(self):
        """
        退出app
        self.driver.background_app(pkg)
        self.driver.is_app_installed(pkg)
        self.driver.install_app(pkg)
        self.driver.remove_app(pkg)
        self.driver.terminate_app(pkg)
        self.driver.activate_app(pkg)
        self.driver.query_app_state(pkg)
        self.driver.app_strings(pkg)
        :return:
        """
        if self.driver:
            # self.driver.close_app()  # 没有用
            pkg = 'com.cmschina.cmschina_hk_app'
            app_id = self.driver.current_package
            print("appid", app_id)
            self.driver.terminate_app(app_id)  # 退出app进程，虽然退出比较快，但是重新登录时会有5秒广告，增加登录时长
            # self.driver.background_app(pkg)
            pkg_state = self.driver.query_app_state(pkg)

    def clear(self):
        if self.driver:
            self.driver.quit()

    def touch_action(self):
        from appium.webdriver.common.touch_action import TouchAction
        # 执行向后滑动操作
        action = TouchAction(self.driver)
        # 设置起始点坐标和终点坐标
        start_x = 500
        start_y = 1500
        end_x = 500
        end_y = 500
        # 执行滑动操作
        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

        # 等待一段时间，让页面响应
        time.sleep(2)


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = XhjTradeBot()

    def tearDown(self) -> None:
        self.bot.clear()

    def test_find_element(self):
        el = self.bot.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Logout)
        el.get_attribute('displayed')
        print('---->', el, 'displayed>>', el.get_attribute('displayed'))

    def test_on_aciton(self):
        self.bot.touch_action()

    @unittest.skip('')
    def test_get_capture(self):
        self.bot.get_image_capture()

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

    @unittest.skip('')
    def test_back_index_page(self):
        self.bot.back_index_page()

    @unittest.skip('')
    def test_logout(self):
        self.bot.logout()

    @unittest.skip('')
    def test_logout_app(self):
        self.bot.logout_app()


if __name__ == '__main__':
    unittest.main()


