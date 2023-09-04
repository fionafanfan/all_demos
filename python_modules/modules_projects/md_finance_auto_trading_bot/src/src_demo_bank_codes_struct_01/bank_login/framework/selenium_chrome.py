#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/4 17:34
# @File     : selenium_chrome.py
# @Desc     :
import os
from collections import namedtuple

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
# selenium chrome功能：
打开相关银行登录页面
获取相对应的数据： 持仓、流水、订单、回单
执行一些操作： 下单、撤单

无关业务的功能：
定位元素
执行js
获取验证码
截图
保存截图

# selenium driver相关变量：
"""
opts = config("nodes", "browser_driver", "chrome_options")
config('nodes', 'browser_driver', 'page_load_timeout')

_IMPLICIT_WAIT_TIME = 10  # 全局隐式等待时间
_EXPLICIT_WAIT_TIME = 3  # 全局显示等待时间


# 元素定位信息
ElementSelect = namedtuple('ElementSelector', [
    # 名称、定位方法(By.XPATH、By.CSS_SELECTOR)、选择表达式、期望状态
    # 期望状态: clickable、visible、located、text(内容不为空)
    'name', 'method', 'selector', 'status'
])


class SeleniumDriver(object):
    is_need_driver = True

    def __init__(self):
        self._driver: webdriver.Chrome = None
        self._close_page_source = ''

    def __init(self):
        if self.is_need_driver:
            self._init_driver()
            self._wait = _MyWebDriverWait(self.driver, _EXPLICIT_WAIT_TIME, ignored_exceptions=(NoSuchElementException,
                                                                                                KeyboardInterrupt))

    def _init_driver(self):
        """
        浏览器驱动初始化
        """
        chrome_options = Options()
        opts = config("nodes", "browser_driver", "chrome_options")
        for opt, enable in opts.items():
            if enable:
                chrome_options.add_argument(opt)
        # 下载路径
        prefs_experimental_options = {'download.default_directory': self.disk_cache.cache_dir,
                                      'savefile.default_directory': self.disk_cache.cache_img_dir}
        chrome_options.add_experimental_option('prefs', prefs_experimental_options)
        if os.getenv('WDM_SSL_VERIFY') != '0':
            os.environ['WDM_SSL_VERIFY'] = '0'  # 防止webdriver_manager在首次执行下载driver时报SSL错误, 此库官网提供的解决方案
        self._driver = webdriver.Chrome(ChromeDriverManager(path = utils.abs_path('packages', 'windows', 'auto_chrome_drivers'),
                                                            cache_valid_range=3650).install(),
                                        chrome_options=chrome_options,
                                        **self.chrome_driver_init_params())
        self._driver.implicitly_wait(_IMPLICIT_WAIT_TIME)
        self._driver.set_page_load_timeout(config('nodes', 'browser_driver', 'page_load_timeout'))

    @property
    def driver(self) -> Chrome:
        return self._driver

    def chrome_driver_init_params(self):
        """
        自定义chrome driver初始化参数，子类中如果有除chrome_options外特定参数如desired_capabilities
        可以重写此方法
        :return dict: webdriver.Chrome关键字参数
        """
        return {}

    def js_click(self, e):
        """
        通过执行脚本点击
        """
        self.driver.execute_script('arguments[0].click();', e)

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

    def select_element(self, element_selects: [ElementSelect], wait_time=10):
        """
        选择元素
        """
        max_wait_time = gApp.current_time + wait_time
        name = ''
        element_selects = [element_selects] if not isinstance(element_selects, list) else element_selects
        while not name and gApp.current_time < max_wait_time:
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
                    if element_select.method == By.XPATH:
                        check_func = self.driver.find_element_by_xpath
                    else:
                        check_func = self.driver.find_element_by_css_selector
                    if len(check_func(element_select.selector).text) > 0:
                        name = element_select.name
                        break
                else:
                    continue
                if check_func(element_select.method, element_select.selector, wait_time=0.5):
                    name = element_select.name
                    break
        return name

    def get_current_screenshot(self):
        """
        获取当前页面截屏数据
        :return: PIL.Image 对象
        """
        screenshot = self.driver.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))

        return screenshot

    def save_current_screenshot(self, image_name=''):
        """
        保存当前截屏
        :param image_name: 图片名称
        """
        sc = self.get_current_screenshot()
        image_name = image_name if image_name else f'{self.bank_code}_{self.account_id}'
        self.save_image(sc, image_name)

    @staticmethod
    def save_image(img: Image, name):
        """
        保存图像
        :param img: Image对象
        :param name: 图片名称
        """
        dir_img = os.path.join(utils.root_path(), 'images')
        os.makedirs(dir_img, exist_ok=True)
        img_path = os.path.join(dir_img, f"{name}.png")

        with open(img_path, 'wb') as f:
            img.save(f)

    @staticmethod
    def save_html(html, name, encoding='utf-8'):
        """
        保存html
        :param html: html字符串
        :param name: html名称
        :param encoding: 编码
        """
        dir_html = os.path.join(utils.root_path(), 'html')
        os.makedirs(dir_html, exist_ok=True)
        html_path = os.path.join(dir_html, f"{name}.html")

        with open(html_path, 'w', encoding=encoding) as f:
            f.write(str(html))

    @staticmethod
    def calc_screen_zom_scale():
        def get_real_resolution():
            """
            获取真实分辨率
            :return:
            """
            hDC = win32gui.GetDC(0)

            w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
            h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
            return w, h

        def get_screen_size():
            """
            获取缩放后的分辨率
            :return:
            """
            w = GetSystemMetrics(0)
            h = GetSystemMetrics(1)
            return w, h

        real_px = get_real_resolution()
        resize_px = get_screen_size()
        scale_rate = real_px[0] / resize_px[0]

        return scale_rate

    def get_element_screenshot(self, element, save=True, name='captcha'):
        """
        获取元素截屏
        :param element: selenium页面元素对象
        :param save: 是否保存截屏到本地
        :param name: 保存截屏名称
        :return: base64编码数据
        """
        def _get_position():
            location = element.location
            size = element.size

            # 元素左，上，右，下，的坐标值
            left, top = location['x'], location['y']
            left, top = left * scale, top * scale  # 由于屏幕可能会缩放，因此坐标也应缩放相同的比例

            right, bottom = left + size['width'] * scale, top + size['height'] * scale

            return left, top, right, bottom

        scale = self.calc_screen_zom_scale()
        position = _get_position()
        sc = self.get_current_screenshot().crop(position)
        if save:
            self.save_image(sc, name)

        byte_buffer = BytesIO()
        sc.save(byte_buffer, format='PNG')
        data = byte_buffer.getvalue()
        base64_data = base64.b64encode(data).decode()

        return base64_data

    def get_captcha_with_url(self, url, headers=None, save=True, name='captcha'):
        """
        获取元素截屏
        :param url: 验证码url地址
        :param headers: 验证码url请求头
        :param save: 是否保存图片到本地
        :param name: 保存截屏名称
        :return: base64编码数据
        """
        http_client = self.get_session_with_cookie()
        if headers:
            ret = http_client.get(url, headers=headers)
        else:
            ret = http_client.get(url)

        base64_data = base64.b64encode(ret.content).decode()
        if save:
            img = Image.open(BytesIO(ret.content))
            self.save_image(img, f'{self.account_id}_{name}')
        return base64_data

    def close(self):
        if self.driver:
            try:
                # 保存退出时的截屏
                self.save_current_screenshot(f'{self.bank_code}_{self.account_id}_close_page')
                self._close_page_source = self.driver.page_source
                self.driver.quit()
            except:
                pass
