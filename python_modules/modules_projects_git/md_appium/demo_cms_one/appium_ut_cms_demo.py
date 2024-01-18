#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/27 16:43
# @File     : appium_ut_cms_demo.py
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

from messages import LoginRequestMsg
from messages import ServerEventIdType


capabilities = {
  "platformName": "Android",
  "automationName": "uiautomator2",
  "appium:newCommandTimeout": 0,
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
    login_my_account = 'descriptionContains("我的账户")'  # 组合定位界面登录界面的
    login_button = 'descriptionContains("我的账户").descriptionContains("登录")'  # 登录触发按钮元素
    after_login = 'descriptionContains("我的账户").descriptionContains("已登录")'  # 已登录

    login_page_title = 'descriptionContains("交易登录").index(1)'  # 交易登录页的标题
    login_user = f'//android.view.View[@content-desc="证券账户"]/following-sibling::android.view.View[1]'  # 交易账户-如果进入交易登录页，账号是固定的;
    # 传入账号进行比对88811489， 如果找得到，则代表账号输入正确
    login_passwd = '//android.view.View[@content-desc="登录密码"]/following-sibling::android.widget.EditText[1]'  # 交易账户-密码; xpath locator
    read_agreement = 'descriptionContains("已阅读并同意")'  # 已阅读协议, self.driver.tap([tuple(e.location_in_view.values())])
    login_submit = '//android.widget.Button[@content-desc="交易登录"]'  # 交易登录请求提交
    passwd_error = '//android.view.View[@content-desc="登录密码不正确"]'  # 登录密码不正确

    # 登录图形验证码-(前置动作 和 首次完成手机号登录，再输入密码登录 都有, 但只需要考虑后者，元素定位都是一样的)
    image_capture = '//android.widget.ImageView[@content-desc="看不清？点击换一个"]'  # 图形验证码图片
    image_capture_update = '//android.widget.ImageView[@content-desc="看不清？点击换一个"]'  # 刷新图形验证码
    image_capture_input = 'textContains("请输入图形验证码")'  # 请输入图形验证码
    image_capture_input_check = 'descriptionContains("确 定")'  # 输入图形验证码确认
    capture_error_lock = '//android.view.View[@content-desc="验证码错误次数过多"]/android.view.View/android.view.View'
    capture_error = '//android.view.View[@content-desc="图形验证码错误"]/android.view.View/android.view.View'

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

    登录：
       登录前
       登录成功后
       可交易
    交易
    登出

    if self.is_in_page(self.Page.LoginSuccess):
        print("保持心跳")
    else:
        print("停止心跳”）

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
        13-启动连接成功: 返回启动连接成功信息，同时去检测当前是否已完成前置动作。
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


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = CmsBot()

    def tearDown(self) -> None:
        self.bot.clear()

    # def test_find_element(self):
    #     el = self.bot.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Logout)
    #     el.get_attribute('displayed')
    #     print('---->', el, 'displayed>>', el.get_attribute('displayed'))
    #
    # def test_page_name(self):
    #     page_name = self.bot.check_page_name(name='my_page')
    #     print('page_name', page_name)
    #     # page_name = self.bot.select_element([ElementSelector(name='my_activity',
    #     #                                          method=AppiumBy.ANDROID_UIAUTOMATOR,
    #     #                                      selector='descriptionContains("活动中心")',
    #     #                                      status='display')], wait_time=1)
    #     # print('page_name', page_name)

    @unittest.skip('')
    def test_get_capture(self):
        self.bot.get_image_capture()

    # @unittest.skip('')
    def test_login_start_conn(self):
        self.bot.login_start_conn()

    @unittest.skip('')
    def test_login_with_account(self):
        self.bot.login_with_account()

    @unittest.skip('')
    def test_login_with_img_capture(self):
        self.bot.login_with_img_capture()

    @unittest.skip('')
    def test_login_with_otp(self):
        self.bot.login_with_otp()

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

    # @unittest.skip('')
    def test_logout_app(self):
        self.bot.logout_app()


if __name__ == '__main__':
    unittest.main()


