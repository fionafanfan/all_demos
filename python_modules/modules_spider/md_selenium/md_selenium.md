# selenium 

截至2023-10-18 最新发布版本为：selenium 4.14.0 （2023-10-10发布）
pypi地址：https://pypi.org/project/selenium/
python 3.6版本 能够安装的最新的selenium的版本为 3.7.1版本，
要想安装更高的版本， 则要求python>=3.7

selenium:
- home: https://selenium.dev
- GitHub: https://github.com/SeleniumHQ/Selenium
- PyPI: https://pypi.org/project/selenium/
- IRC/Slack: https://www.selenium.dev/zh-cn/documentation/
 

webdriver的方式:
- putting the driver in the PATH
- using system properties
- rely on a third-paty driver manager to do it automatically
  - web chromedriver download url
    - 最新的chromdirver版本114.0.5735.90下载站点地址: https://sites.google.com/chromium.org/driver/downloads   
      - chromedriver版本列表选项首页：https://chromedriver.storage.googleapis.com/index.html 
      - 具体某个版本的下载的真正地址：https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/
      - 旧地址支持最新的版本是114.0.5735.90: https://chromedriver.storage.googleapis.com/LATEST_RELEASE
    - chromdirver115及以上版本及chrome浏览器站点下载地址： https://googlechromelabs.github.io/chrome-for-testing/
    - chromdirver115及以上版本及chrome浏览器站点下载地址json文件：https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
    - https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5740.0/win64/chrome-win64.zip
    - https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5763.0/win64/chromedriver-win64.zip
  - 从4.11.0开始 selenium实现了对浏览器的版本自动管理, 支持的浏览器列表及地址  
    - Chrome:  https://googlechromelabs.github.io/chrome-for-testing/
    - Firefox:
    - Edge: 

查看webdriver manager源码：
```python
# down_webdriver_url_format = f"{self._url}/{self.get_version()}/{self.get_name()}_{self.get_os_type()}.zip"
url = "https://chromedriver.storage.googleapis.com"
version = "114.0.5735.90"
name = "chromedriver"
os_type = "win32"
down_webdriver_url_format = f"{url}/{version}/{name}_{os_type}.zip"
# 这个链接get方法，可以下载指定版本的chromedriver文件
down_webdriver_url = "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_win32.zip" 
latest_release_url="https://chromedriver.storage.googleapis.com/LATEST_RELEASE"

# webdriver_manager.core.download_manager
class DownloadManager(object):
    pass


class WDMDownloadManager(DownloadManager):
     def download_file(self):
          url = ""
          

class DriverCache(object):
    pass


class DriverManager(object):
    pass

    def _get_driver_path(self, driver):
        pass 
        # 下载driver的入口
        # file = self._download_manager.download_file(driver.get_url())
        # binary_path = self.driver_cache.save_file_to_cache(driver, file)

    
class ChromeDriverManager(DriverManager):
    pass

# webdriver_manager.core.driver
class Driver(object):
    def get_url(self):
        return down_webdriver_url_format



class ChromeDriver(Driver):
    pass

"""
提示语：
latest_release_url="https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
ValueError: There is no such driver by url https://chromedriver.storage.googleapis.com/LATEST_RELEASE_118.0.5993

应该是可以自己自定义download_manager吧。
self._download_manager = download_manager
if download_manager is None:
    self._download_manager = WDMDownloadManager()
    
self._driver = webdriver.Chrome(ChromeDriverManager(path = utils.abs_path('packages', 'windows', 'auto_chrome_drivers'),
                                                    cache_valid_range=3650).install(),
                                chrome_options=chrome_options,
                                **self.chrome_driver_init_params())
self._driver.implicitly_wait(_IMPLICIT_WAIT_TIME)
"""
```
- webdriver_manager
  - core
    - download_manager.py
      - DownloadManager 
      - WDMDownloadManager(DownloadManager)
    - driver.py 
      - Driver 
    - manager.py 
      - DriverManager
    - http.py 
      - HttpClient 
      - WDMHttpClient(HttpClient)
  - drivers
    - chrome.py
      - ChromeDriver(Driver)
  - chrome.py 
    - ChromeDriverManager(DriverManager)
    - ChromeDriver
