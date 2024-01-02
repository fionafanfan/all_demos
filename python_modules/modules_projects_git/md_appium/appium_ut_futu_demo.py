"""
appium
"""
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


capabilities = {
  "platformName": "Android",
  "appium:automationName": "uiautomator2",
  "appium:appium.options": {
    "automationName": "uiautomator2",
    "deviceName": "192.168.0.172:5555",
    "noRes": True
  },
  "appium:appPackage": "cn.futu.trader",
  "appium:appActivity": "cn.futu.trader.launch.activity.LaunchActivity",
  "appium:appium.settings": {
    "ignoreUnimportantViews": True,
    "allowInvisibleElements": True
  },
  "appium:noReset": False
}


appium_server_url = 'http://localhost:4723'


class Login(object):
    """
    ��¼���̣�
    1��δ���ǰ�ò����� �������ǰ�ò���
    2. �����ǰ�ò�����

    ���Ǵ��󳡾���ʾ
    1. �˺������������
    2. ͼ����֤��������󡢿�����ˢ����֤�롢��ʱ
    3. otp������� ��������������ʱ

    ͼ����֤���������������࣬�ᱻ��������ס1Сʱ  (��֤�����������࣬����21����)
    ������֤��opt, ���͵����ţ���֤��5��������Ч�� ҳ���ط���ȴ�60s���������·�����֤��
    """
    login_phone_button = 'descriptionStartsWith("��¼/ע��")'  # �ֻ��ŵ�¼ע��
    login_button = 'descriptionContains("�ҵ��˻�").descriptionContains("��¼")'  # ��¼������ťԪ��
    after_login = 'descriptionContains("�ҵ��˻�").descriptionContains("�ѵ�¼")'  # �ѵ�¼

    login_page_title = 'descriptionContains("���׵�¼").index(1)'  # ���׵�¼ҳ�ı���
    login_user = f'//android.view.View[@content-desc="account"]'  # �����˻�-������뽻�׵�¼ҳ���˺��ǹ̶���;
    # �����˺Ž��бȶ�88811489�� ����ҵõ���������˺�������ȷ
    login_passwd = '//android.widget.EditText[@text="�������¼����"]'  # �����˻�-����; xpath locator
    read_agreement = 'descriptionContains("���Ķ���ͬ��")'  # ���Ķ�Э��, self.driver.tap([tuple(e.location_in_view.values())])
    login_submit = 'descriptionContains("���׵�¼").index(7)'  # ���׵�¼�����ύ

    # ��¼ͼ����֤��-(ǰ�ö��� �� �״�����ֻ��ŵ�¼�������������¼ ����, ��ֻ��Ҫ���Ǻ��ߣ�Ԫ�ض�λ����һ����)
    image_capture = '//android.widget.ImageView[@content-desc="�����壿�����һ��"]'  # ͼ����֤��ͼƬ
    image_capture_update = '//android.widget.ImageView[@content-desc="�����壿�����һ��"]'  # ˢ��ͼ����֤��
    image_capture_input = 'textContains("������ͼ����֤��")'  # ������ͼ����֤��
    image_capture_input_check = 'descriptionContains("ȷ ��")'  # ����ͼ����֤��ȷ��
    capture_error = '//android.view.View[@content-desc="��֤������������"]/android.view.View/android.view.View'

    # ������֤��opt
    otp_input = '//android.view.View[3]'  # otp����
    otp_check = 'descriptionContains("ȷ ��")'  # otp�ύ


class Logout(object):
    """
    �ǳ�����
    """
    logout_button = 'descriptionContains("�˻�����").descriptionContains("�˳���¼")'  # �˳���¼��ť
    check_logout_yes_button = 'descriptionContains("ȷ���˳�")'  # ȷ���Ƿ�Ҫ�˳�
    check_logout_cancel_button = 'descriptionContains("ȡ��")'  # ȡ���˳�
    check_logout_content = 'descriptionContains("�˳��������޷����׻�鿴�ֲ���Ϣ����ȷ���Ƿ���Ҫ�˳�")'


class MyAppium(object):
    pass


class CmsBot(object):
    """
    ���̹���app�汾
    """
    def login(self):
        """
        ��¼
        :return:
        """
        pass

    def logout(self):
        """
        �ǳ�
        :return:
        """
        pass

    def check_page(self):
        """ȷ�ϵ�ǰ���ĸ�ҳ��"""
        pass


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

    def test_find_capture_error(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="��֤������������"]/android.view.View/android.view.View')
        print(el)

    def test_input(self):
        pass
        # self.driver.find_element(AppiumBy.ID,'com.wetrade.financial:id/etUserName').send_keys('test')

    def test_login(self):
        pass

    def test_logout(self):
        pass

    def test_check_page(self):
        pass


if __name__ == '__main__':
    unittest.main()

