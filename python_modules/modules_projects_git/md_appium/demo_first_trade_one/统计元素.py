#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/4/20 17:07
# @File     : 统计元素.py
# @Desc     :
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy

# 初始化 Appium 驱动
capabilities = {
  "platformName": "Android",
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
  "appPackage": "com.firstsechk.tc.trade",
  "appActivity": "com.afe.mobilecore.tcuicore.SplashBaseActivity",
  "appium.settings": {
    "ignoreUnimportantViews": True,
    "allowInvisibleElements": True
  },
  "noReset": True
}

appium_server_url = 'http://localhost:4723'


driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

print("driver启动app成功")

# 使用 XPath 查找父元素
parent_element_el = driver.find_element(AppiumBy.XPATH, '//android.widget.ListView[@resource-id="com.firstsechk.tc.trade:id/custom_wrapped_section_listview"]')
# parent_elements = parent_element_el.find_elements(AppiumBy.XPATH, '../*')
parent_elements = parent_element_el.find_elements(AppiumBy.XPATH, ".//android.widget.RelativeLayout")  # '//android.widget.ListView[@resource-id="com.firstsechk.tc.trade:id/custom_wrapped_section_listview"]/android.widget.RelativeLayout[2]'
# 找到父元素下的所有子元素
holdings = []
for parent_element in parent_elements[1:]:
    stock_code = parent_element.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lbl_Symbol"]')[0].text
    price = parent_element.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lbl_Price"]')[0].text
    holding_qty = parent_element.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lbl_AvailQty"]')[0].text
    market = parent_element.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.firstsechk.tc.trade:id/lbl_Exchg"]')[0].text
    holding = {'stock_code': stock_code, 'price': price, 'holding_qty': holding_qty, 'market': market}
    holdings.append(holding)

print(holdings)
print('end')

"""
[
{'stock_code': '00063', 'price': '0.088', 'holding_qty': '7,000', 'market': '香港'}, 
{'stock_code': 'CATO', 'price': '5.648', 'holding_qty': '5', 'market': 'US'}, 
{'stock_code': 'CSPI', 'price': '20.395', 'holding_qty': '2', 'market': 'US'}, 
{'stock_code': 'NYMT', 'price': '7.326', 'holding_qty': '5', 'market': 'US'}
]
"""
