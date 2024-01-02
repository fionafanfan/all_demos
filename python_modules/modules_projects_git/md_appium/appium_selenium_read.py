#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/25 16:35
# @File     : appium_selenium_read.py
# @Desc     :
"""
动作链是一种自动化低级交互(如鼠标)的方法
移动、鼠标按钮操作、按键和上下文菜单交互。
这对于执行更复杂的操作(如悬停和拖动)非常有用
下降。
生成用户操作。
当你调用ActionChains对象上动作的方法时，
动作存储在ActionChains对象的队列中。
当您调用perform()时，事件将按照它们的顺序触发
都在排队。
ActionChains可以用于链式模式::

demo：
    menu = driver.find_element(By.CSS_SELECTOR, ".nav")
    hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

    actions = ActionChains(driver)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
"""