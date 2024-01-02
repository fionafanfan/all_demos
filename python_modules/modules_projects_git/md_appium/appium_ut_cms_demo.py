"""
appium
"""
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='9236a8a2',
    appPackage='com.cmschina.cmschina_hk_app',
    appActivity='com.cmschina.cmschina_hk_app.MainActivity',
    noRest=True
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    @unittest.skip('')
    def test_find_battery(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[text="Battery"]')
        el.click()

    def test_input(self):
        pass
        # self.driver.find_element(AppiumBy.ID,'com.wetrade.financial:id/etUserName').send_keys('test')


if __name__ == '__main__':
    unittest.main()

