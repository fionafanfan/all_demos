# selenium 

����2023-10-18 ���·����汾Ϊ��selenium 4.14.0 ��2023-10-10������
pypi��ַ��https://pypi.org/project/selenium/
python 3.6�汾 �ܹ���װ�����µ�selenium�İ汾Ϊ 3.7.1�汾��
Ҫ�밲װ���ߵİ汾�� ��Ҫ��python>=3.7

selenium:
- home: https://selenium.dev
- GitHub: https://github.com/SeleniumHQ/Selenium
- PyPI: https://pypi.org/project/selenium/
- IRC/Slack: https://www.selenium.dev/zh-cn/documentation/
 

webdriver�ķ�ʽ:
- putting the driver in the PATH
- using system properties
- rely on a third-paty driver manager to do it automatically
  - web chromedriver download url
    - ���µ�chromdirver�汾114.0.5735.90����վ���ַ: https://sites.google.com/chromium.org/driver/downloads   
      - chromedriver�汾�б�ѡ����ҳ��https://chromedriver.storage.googleapis.com/index.html 
      - ����ĳ���汾�����ص�������ַ��https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/
      - �ɵ�ַ֧�����µİ汾��114.0.5735.90: https://chromedriver.storage.googleapis.com/LATEST_RELEASE
    - chromdirver115�����ϰ汾��chrome�����վ�����ص�ַ�� https://googlechromelabs.github.io/chrome-for-testing/
    - chromdirver115�����ϰ汾��chrome�����վ�����ص�ַjson�ļ���https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
    - https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5740.0/win64/chrome-win64.zip
    - https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5763.0/win64/chromedriver-win64.zip
  - ��4.11.0��ʼ seleniumʵ���˶�������İ汾�Զ�����, ֧�ֵ�������б���ַ  
    - Chrome:  https://googlechromelabs.github.io/chrome-for-testing/
    - Firefox:
    - Edge: 

�鿴webdriver managerԴ�룺
```python
# down_webdriver_url_format = f"{self._url}/{self.get_version()}/{self.get_name()}_{self.get_os_type()}.zip"
url = "https://chromedriver.storage.googleapis.com"
version = "114.0.5735.90"
name = "chromedriver"
os_type = "win32"
down_webdriver_url_format = f"{url}/{version}/{name}_{os_type}.zip"
# �������get��������������ָ���汾��chromedriver�ļ�
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
        # ����driver�����
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
��ʾ�
latest_release_url="https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
ValueError: There is no such driver by url https://chromedriver.storage.googleapis.com/LATEST_RELEASE_118.0.5993

Ӧ���ǿ����Լ��Զ���download_manager�ɡ�
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
