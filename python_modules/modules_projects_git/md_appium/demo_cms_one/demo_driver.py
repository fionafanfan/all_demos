#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/9 10:35
# @File     : demo_driver.py
# @Desc     :
class Bot(object):

    is_need_driver = True

    def __init__(self):
        print("-- webdriver_chrome_driver  初始化 --")
        self._driver = 'webdriver_chrome_driver'

    @property
    def driver(self):
        return self._driver

    def close(self):
        print('Bot 关闭操作')


class AppiumAndroidDriver(object):

    def __init__(self):
        print("-- AppiumAndroidDriver 初始化--")
        self._driver = 'appium_android_driver'

    @property
    def driver(self):
        return self._driver

    def close_driver(self):
        print(self.driver, "  关闭")


class CMSInternational(AppiumAndroidDriver, Bot):
    def __init__(self):
        self.is_need_driver = False  # 不需要chromedriver

        Bot.__init__(self)
        AppiumAndroidDriver.__init__(self)

    def print_driver(self):
        print('use driver>>', self.driver)

    def logout(self):
        print("手动退出")

    def close_driver(self):
        super(CMSInternational, self).close_driver()

    def close(self):
        super(CMSInternational, self).close()
        print("关闭操作后续操作")
        self.logout()
        self.close_driver()


cms_bot = CMSInternational()
cms_bot.print_driver()
cms_bot.close()

