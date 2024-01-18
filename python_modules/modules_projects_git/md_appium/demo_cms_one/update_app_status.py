#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/9 17:25
# @File     : update_app_status.py
# @Desc     :
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from appium.options.android import UiAutomator2Options


capabilities = {
  "platformName": "Android",
  "automationName": "uiautomator2",
  "appium:newCommandTimeout": 0,
  "appium.options": {
    # "automationName": "uiautomator2",
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


driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

print("driver启动app成功")


# 导入 TouchAction 类
from appium.webdriver.common.touch_action import TouchAction

# 找到下拉刷新元素，假设它有 id 为 "pull_to_refresh", 得要找到下拉按钮
pull_to_refresh = driver.find_element("pull_to_refresh")

# 模拟下拉刷新
action = TouchAction(driver)
action.press(x=50, y=100).move_to(x=50, y=500).release().perform()
