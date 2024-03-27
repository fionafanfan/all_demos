#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/18 11:28
# @File     : selm_webdriver_manager.py
# @Desc     : selenium webdriver manager
import os

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


_IMPLICIT_WAIT_TIME = 10  # 全局隐式等待时间
_EXPLICIT_WAIT_TIME = 3  # 全局显示等待时间


def root_path():
    """
    项目根目录
    """
    abs_path = os.path.abspath(__file__)
    rootpath = os.path.dirname(abs_path)
    rootpath = os.path.dirname(rootpath)
    return rootpath


def abs_path(*args):
    """
    绝对路径
    """
    return os.path.join(root_path(), *args)


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


class SeleniumManager(object):
    is_need_driver = True

    def __init__(self):
        self._driver: webdriver.Chrome = None
        self._wait: _MyWebDriverWait = None
        self._disk_cache = None
        self.__init()

    def __init(self):
        if self.is_need_driver:
            self._init_driver()
            # self._wait = _MyWebDriverWait(self.driver, _EXPLICIT_WAIT_TIME,
            # ignored_exceptions=(NoSuchElementException,
            # KeyboardInterrupt))
            self._wait = _MyWebDriverWait(self.driver, _EXPLICIT_WAIT_TIME)

    def _init_driver(self):
        """
        浏览器驱动初始化
        """
        chrome_options = Options()
        browser_driver = {
                    "chrome_options": {
                      "--headless": False,
                      "--disable-gpu": True,
                      "blink-settings=imagesEnabled": True,
                      "--start-maximized": True  # 设置浏览器默认以最大化窗口运行 local
                    }
                  }
        # opts = config("nodes", "browser_driver", "chrome_options")
        opts = browser_driver.get("chrome_options", {})
        for opt, enable in opts.items():
            if enable:
                chrome_options.add_argument(opt)
        if os.getenv('WDM_SSL_VERIFY') != '0':
            os.environ['WDM_SSL_VERIFY'] = '0'  # 防止webdriver_manager在首次执行下载driver时报SSL错误, 此库官网提供的解决方案
        self._driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=3650).install(), chrome_options=chrome_options)
        self._driver.implicitly_wait(_IMPLICIT_WAIT_TIME)

    # selenium 相关
    @property
    def driver(self) -> Chrome:
        return self._driver


class Bot(SeleniumManager):

    def __init__(self):
        super(Bot, self).__init__()
        self.__init()

    def __init(self):
        if self.is_need_driver:
            self._init_driver()
            self._wait = _MyWebDriverWait(self.driver, _EXPLICIT_WAIT_TIME)


class TestBaiduBot(Bot):

    def __init__(self):
        super(TestBaiduBot, self).__init__()
        self.start_url = "http://www.baidu.com"

    def open_start_page(self, refresh=True):
        """
        测试打开开始页面
        """
        if refresh:
            self.driver.get(self.start_url)



