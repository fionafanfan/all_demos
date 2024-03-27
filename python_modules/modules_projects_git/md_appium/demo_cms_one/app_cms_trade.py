#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/9 17:25
# @File     : update_app_status.py
# @Desc     :
import time
from datetime import datetime
import enum
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
  "platformName": "Android",
  "automationName": "uiautomator2",
  "appium:newCommandTimeout": 0,
  "appium.options": {
    # "automationName": "uiautomator2",
    "deviceName": "10.18.20.13:5555",
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

# appium_server_url = 'http://172.16.22.26:4723'
appium_server_url = 'http://localhost:4723'


driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

print("driver启动app成功")
input_phone_xpath = '//android.widget.EditText[@text="请输入手机号"]'

last_log_time = None
consume_times = []
log_file = open(f'logfile/appium_ut_demo.log', 'a')


def myprint_raw(s):
    now = datetime.now()
    cur_time = now.strftime('%Y/%m/%d %H:%M:%S.%f')
    print(f'【{int(now.timestamp()*1000)}】【{cur_time}】_{s}')


def myprint(msg, level='INFO', calc_time=None):
    global last_log_time
    now = datetime.now()
    format_msg = f'{now} [{level}] {msg}'

    calc_time = calc_time if calc_time is not None else msg.find('[end') != -1
    if calc_time:
        time_delta = now - last_log_time
        consume_time = time_delta.total_seconds()
        format_msg += f' {consume_time}'
        consume_times.append((msg, consume_time))

    print(format_msg)
    print(format_msg, file=log_file)

    last_log_time = now


def input_phone():
    myprint('--- begin ---')
    input_phone_el = driver.find_element(by=AppiumBy.XPATH, value=input_phone_xpath)
    myprint('--- [input_phone_el][find_element][end] ---')
    input_phone_el.clear()
    myprint('--- [input_phone_el][clear][end] ---')
    input_phone_el.click()
    myprint('--- [input_phone_el][click][end] ---')
    input_phone_el.send_keys('12345678')
    myprint('--- end ---')


class Trade:
    """
    交易
    """
    INPUT_STOCK = 'textContains("请输入代码").index(0)'
    INPUT_PRICE = 'textContains("请输入价格")'
    INPUT_AMOUNT = 'textContains("请输入数量")'
    BUTTON_BUY = 'description("买入")'
    BUTTON_SELL = 'description("卖出")'
    TEXT_TRADE_CONFIRM = 'descriptionContains("订单确认")'
    TEXT_NO_MONEY = 'descriptionContains("购买力不足")'
    TEXT_NO_HOLDING = 'descriptionContains("持仓不足")'
    TEXT_MIN_PRICE_UNIT_WARN = 'descriptionContains("最小价格单位提醒")'
    BUTTON_CANCEL = 'description("取消")'
    BUTTON_CONTINUE = 'descriptionContains("继续")'
    MENU_ORDER = 'descriptionStartsWith("订单")'
    SCROLL = 'className("android.widget.ScrollView")'

    # xpath
    TEXT_DIR = '//android.view.View[contains(@content-desc, "方向")]/following-sibling::android.view.View[1]'


@enum.unique
class TradingDirection(enum.IntEnum):
    """
    交易方向
    """
    Buy = 0  # 买
    Sell = 1    # 卖
    SellAll = 2  # 全卖


def get_app_element_part_position(e: webdriver.webelement.WebElement, part='front_center'):
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


def raw_trade():
    # 输入股票代码
    stock_code = '00700.hk'

    myprint(f"[timeit] [buy_or_sell] [input_stock_code][start] ")

    myprint('--- [e_stock_code][find_element][start] ---')
    e_stock_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Trade.INPUT_STOCK)
    myprint('--- [e_stock_code][find_element][end] ---')

    myprint('--- [e_stock_code][click][start] ---')
    e_stock_code.click()
    myprint('--- [e_stock_code][click][end] ---')

    myprint('--- [e_stock_code][clear][start] ---')
    e_stock_code.clear()
    myprint('--- [e_stock_code][clear][end] ---')

    myprint('--- [e_stock_code][send_keys][start] ---')
    e_stock_code.send_keys(stock_code)
    myprint('--- [e_stock_code][send_keys][end] ---')

    myprint(f"[timeit][buy_or_sell] [input_stock_code][end] ")

    # 选择交易方向
    myprint(f"[timeit][buy_or_sell] [dir] [start] ")
    e_dir = driver.find_element(AppiumBy.XPATH, Trade.TEXT_DIR)
    # 模拟点击元素对应位置，前半部为买入按钮位置，后半部为卖出按钮位置
    action = 0
    if action == TradingDirection.Buy:
        driver.tap([tuple(get_app_element_part_position(e_dir, 'front_center'))])
    else:
        driver.tap([tuple(get_app_element_part_position(e_dir, 'back_center'))])
    myprint(f"[timeit][buy_or_sell] [dir] [end] ")

    # 输入价格
    price = 0.01

    myprint(f"[timeit][buy_or_sell] [input_price] [start] ")

    myprint('--- [price][find_element][start] ---')
    e_price = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Trade.INPUT_PRICE)
    myprint('--- [price][find_element][end] ---')

    myprint('--- [price][click][start] ---')
    e_price.click()
    myprint('--- [price][click][end] ---')

    myprint('--- [price][time_sleep][start] ---')
    time.sleep(0.5)
    myprint('--- [price][time_sleep][end] ---')

    myprint('--- [price][clear][start] ---')
    e_price.clear()
    myprint('--- [price][clear][end] ---')

    myprint('--- [price][send_keys][start] ---')
    e_price.send_keys(str(price))
    myprint('--- [price][send_keys][end] ---')

    myprint(f"[timeit][buy_or_sell] [input_price] [end] ")

    # 输入股数
    quantity = 200
    myprint(f"[timeit][buy_or_sell] [input_quantity] [start] ")

    myprint('--- [quantity][find_element][start] ---')
    e_amount = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Trade.INPUT_AMOUNT)
    myprint('--- [quantity][find_element][end] ---')

    myprint('--- [quantity][click][start] ---')
    e_amount.click()
    myprint('--- [quantity][click][end] ---')

    myprint('--- [quantity][time_sleep][start] ---')
    time.sleep(0.5)
    myprint('--- [quantity][time_sleep][end] ---')

    myprint('--- [quantity][clear][start] ---')
    e_amount.clear()
    myprint('--- [quantity][clear][end] ---')

    myprint('--- [quantity][send_keys][start] ---')
    e_amount.send_keys(str(quantity))
    myprint('--- [quantity][send_keys][end] ---')

    myprint(f"[timeit][buy_or_sell] [input_quantity] [end] ")


def demo_trade_1():
    import subprocess
    # 输入股票代码
    stock_code = '00700.hk'

    myprint(f"[timeit] [buy_or_sell] [input_stock_code][start] ")

    myprint('--- [e_stock_code][find_element][start] ---')
    e_stock_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Trade.INPUT_STOCK)
    myprint('--- [e_stock_code][find_element][end] ---')

    myprint('--- [e_stock_code][click][start] ---')
    e_stock_code.click()
    myprint('--- [e_stock_code][click][end] ---')

    myprint('--- [e_stock_code][clear][start] ---')
    e_stock_code.clear()
    myprint('--- [e_stock_code][clear][end] ---')

    myprint('--- [e_stock_code][send_keys][start] ---')
    e_stock_code.send_keys(stock_code)
    myprint('--- [e_stock_code][send_keys][end] ---')

    myprint(f"[timeit][buy_or_sell] [input_stock_code][end] ")

    # 选择交易方向
    myprint(f"[timeit][buy_or_sell] [dir] [start] ")
    e_dir = driver.find_element(AppiumBy.XPATH, Trade.TEXT_DIR)
    # 模拟点击元素对应位置，前半部为买入按钮位置，后半部为卖出按钮位置
    action = 0
    if action == TradingDirection.Buy:
        driver.tap([tuple(get_app_element_part_position(e_dir, 'front_center'))])
    else:
        driver.tap([tuple(get_app_element_part_position(e_dir, 'back_center'))])
    myprint(f"[timeit][buy_or_sell] [dir] [end] ")

    # 输入价格
    price = 0.01

    myprint(f"[timeit][buy_or_sell] [input_price] [start] ")

    myprint('--- [price][find_element][start] ---')
    e_price = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Trade.INPUT_PRICE)
    myprint('--- [price][find_element][end] ---')

    myprint('--- [price][click][start] ---')
    # driver.execute_script("arguments[0].value = '0.03, 请输入价格';", e_price)
    # price_text = e_price.get_attribute('text')
    # print("设置过之后price_text", price_text)
    e_price.click()
    myprint('--- [price][click][end] ---')

    myprint('--- [price][time_sleep][start] ---')
    # time.sleep(0.5)
    print("判断是否回填")
    while True:
        price_text = e_price.get_attribute('text')
        print(f"price_text:{price_text}")
        if price_text == '请输入价格':
            print("等待回填")
            pass
        else:
            break
    print("结束回填成功")
    myprint('--- [price][time_sleep][end] ---')

    myprint('--- [price][clear][start] ---')
    e_price.clear()
    myprint('--- [price][clear][end] ---')

    myprint('--- [price][send_keys][start] ---')
    e_price.send_keys(str(price))
    input_cmd = f'adb shell input text "{str(price)}"'
    subprocess.run(input_cmd, shell=True)
    myprint('--- [price][send_keys][end] ---')

    myprint(f"[timeit][buy_or_sell] [input_price] [end] ")

    # 输入股数
    quantity = 200
    myprint(f"[timeit][buy_or_sell] [input_quantity] [start] ")

    myprint('--- [quantity][find_element][start] ---')
    e_amount = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Trade.INPUT_AMOUNT)
    myprint('--- [quantity][find_element][end] ---')

    myprint('--- [quantity][click][start] ---')
    e_amount.click()  # click不能省掉，否则不能切换输入框， 也无法替换为其它更快的方法
    myprint('--- [quantity][click][end] ---')

    # myprint('--- [quantity][time_sleep][start] ---')
    # # time.sleep(0.5)  # 去掉这个休眠的0.5， 通过观察，价格和股数应该是同时回填的，所以在价格的地方休眠0.5即可。
    # myprint('--- [quantity][time_sleep][end] ---')

    myprint('--- [quantity][clear][start] ---')
    e_amount.clear()
    myprint('--- [quantity][clear][end] ---')

    myprint('--- [quantity][send_keys][start] ---')
    e_amount.send_keys(str(quantity))
    myprint('--- [quantity][send_keys][end] ---')

    myprint(f"[timeit][buy_or_sell] [input_quantity] [end] ")


if __name__ == '__main__':
    # input_phone()
    # raw_trade()  # 原始下单方式
    demo_trade_1()  # 优化demo1
    myprint('耗时统计:\n' + '\n'.join(map(str, sorted(consume_times, key=lambda x: x[1]))), calc_time=False)
    myprint(f'总耗时: {sum([d[1] for d in consume_times])}\n\n')
    driver.quit()  # 退出driver
    log_file.close()
