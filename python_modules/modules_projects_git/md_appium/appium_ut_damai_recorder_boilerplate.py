#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/25 18:32
# @File     : appium_ut_damai_recorder_boilerplate.py
# @Desc     :
# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "uiautomator2",
	"appium:appium.options": {"automationName": "uiautomator2", "deviceName": "192.168.0.149:5555", "noRes": True},
	"appium:appPackage": "cn.damai",
	"appium:appActivity": "cn.damai.launcher.splash.SplashMainActivity",
	"appium:appium.settings": {"ignoreUnimportantViews": True, "allowInvisibleElements": True},
	"appium:noReset": True,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

el2 = driver.find_element(by=AppiumBy.ID, value="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"cn.damai:id/item_text\" and @text=\"2024-01-21 周日 19:30\"]")
el3.click()
el4 = driver.find_element(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@resource-id=\"cn.damai:id/item_flowlayout\"])[6]")
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="cn.damai:id/img_jia")
el5.click()
el5.click()
el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"确定\"]")
el6.click()
el7 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.CheckBox[@resource-id=\"cn.damai:id/checkbox\"])[1]")
el7.click()
el8 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.CheckBox[@resource-id=\"cn.damai:id/checkbox\"])[2]")
el8.click()
el9 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.LinearLayout[@resource-id=\"cn.damai:id/bottom_layout\"]/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout")
el9.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(238, 922)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(401, 917)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(238, 929)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(548, 922)
actions.w3c_actions.pointer_action.release()
actions.perform()


driver.quit()
