# appium

appium git��Ŀ�ֿ⣺ https://github.com/appium/appium
������https://appium.io/

# ʹ�ÿ��ٿ�ʼ
1. ��װ appium: ���ص�ַΪ https://appium.io/docs/en/2.3/quickstart/install/
   ϵͳ����Ҫ��
   1�� macOS/Linux/Windows
   2) Node.js  version >= 18.0.0 
   3) npm version >= 8 
   4)By itself, Appium is relatively lightweight and doesn't have significant disk space or RAM requirements. It can even be run in resource-constrained environments like Raspberry Pi, so long as Node.js is available.
    ���䱾����ԣ�Appium��Խ��ᣬû�������Ĵ��̿ռ��RAM����ֻҪNode.js���ã���������������Դ���޵Ļ��������У���Raspberry Pi��
   ��װ���
    1�� npm i -g appium  
   ���ã�
    ׼��������
      1�� Windows 11
      2�� Node.js version==18.16.1 (node -v)
      3)  npm version==9.5.1 (npm --version)
    ��������ִ�����װappium��npm i -g appium 
    ��װ�ɹ��� ��������ִ��: appium  ����ִ�е�ʱ�� appium version==v2.3.0��
    ִ���������������������� [Appium] Welcome to Appium v2.0.0  �����������ɹ��� appium�������У�
2. ��װ UiAutomator2 Driver  ��git��ַ�� https://github.com/appium/appium-uiautomator2-driver��
   1)�鿴appium git�ֿ��readme.md ����֪��3�а�װdriver�ķ���
        1�� npm��װ�� appium driver install --source=npm appium-xcuitest-driver[@<version>]  ʵ�����npm install -g appium-xcuitest-driver@2.3.0   ��װ�ɹ�
        2) ���ذ�װ
        3�� github��װ: appium driver install uiautomator2
2.1 C:\Users>appium driver list
�� Listing available drivers
- uiautomator2@2.35.0 [installed (npm)]
- xcuitest [not installed]
- mac2 [not installed]
- espresso [not installed]
- safari [not installed]
- gecko [not installed]
- chromium [not installed]
- 
3. ��װ ��׿sdk
   ) ANDROID_HOME
4. appium���������appium server --address 192.168.56.1:4723   --allow-cors

4. д�Լ��Ĳ��Խű�, ��ѡ�Ľű�������
   1�� js
   2) java 
   3) python (��ѡ����python�� �ṩ��ʾ����https://appium.io/docs/en/2.3/quickstart/test-py/)
   4) ruby
   5) .net c# 
   
   python appium�ű����裺
       1����װpython appium�ű������⣺ pip install Appium-Python-Client 
       
    ```python
    import unittest
    from appium import webdriver
    from appium.options.android import UiAutomator2Options
    from appium.webdriver.common.appiumby import AppiumBy
    
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appPackage='com.android.settings',
        appActivity='.Settings',
        language='en',
        locale='US'
    )
    
    appium_server_url = 'http://localhost:4723'
    
    class TestAppium(unittest.TestCase):
        def setUp(self) -> None:
            self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    
        def tearDown(self) -> None:
            if self.driver:
                self.driver.quit()
    
        def test_find_battery(self) -> None:
            el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
            el.click()
    
    if __name__ == '__main__':
        unittest.main()
    ```
   ���������⣺
   1. java������ҪҪ16+�� ���򱨴� devicesһֱoffline 
5. �Լ�ʵ��demo�� ���о���׿�ֻ��ϵĸ�;ţţΪ���ӣ�
   ����app�İ�����
   1. adb shell pm list packages ͨ��pc��cmd��adb�������ֻ������е�app�İ��� 
   2. adb shell pm list packages | findstr futu  �����;�İ����� futu���Լ��²�������ƻẬ�е�����
   ����app��Activity���Ѱ�װ��apk�Ĳ��ҷ���, �ο����ӣ� https://blog.csdn.net/gaogsf/article/details/124472026�� 
   
   1. ����װ��app���ֻ����ӵ��������ϣ�����adb devices,��ʾ�豸
   2. cmd�����У�adb shell logcat > D:/log.log������  
   3. �ֻ��ϴ�appӦ��
   4. Ctrl c �ر�adb logcat������
   5. ��log.log�ļ��������ؼ��֣�����Լ��о���app��MainActivity����LaunchActivity 
   �����ͷ����Ĺؼ��ָ��ݾ�����������¼��֣� ��Ҫ���ҵ�����Ӧ�ó����־��
   ```python
   ������ .LaunchActivity
   
    12-25 14:52:52.773  1459  1495 I StatusBarDisable: setFlags what=0 which=1 pkg=Window{b4fdd53 u0 cn.futu.trader/cn.futu.trader.launch.activity.LaunchActivity}
    12-25 14:52:52.776  1459  1505 I ActivityManager: Displayed cn.futu.trader/.launch.activity.LaunchActivity: +1s195ms
        ������ .MainActivity
    12-25 14:53:15.642  1459  1865 I ActivityManager: START u0 {act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 hwFlg=0x10 cmp=com.cmschina.cmschina_hk_app/.MainActivity bnds=[855,1018][1065,1325]} from uid 10060
    12-25 14:53:15.643  1459  1865 I ActivityManager: ActivityRecord info: ActivityInfo{85c4298 com.cmschina.cmschina_hk_app.MainActivity}
   
    12-25 17:53:53.209  1967  1999 I HCALL   : hcallSyncInstalledAppsRpc({"apps":[{"package":"io.appium.settings","activity":"io.appium.settings.Settings","appLabel":"Appium Settings","versionCode":62,"versionName":"5.2.0","isHomeApp":false},{"package":"com.cmschina.cmschina_hk_app","activity":"com.cmschina.cmschina_hk_app.MainActivity","appLabel":"����֤ȯ����","versionCode":399,"versionName":"3.0.0","isHomeApp":false},{"package":"cn.damai","activity":"cn.damai.launcher.splash.SplashMainActivity","appLabel":"����","versionCode":6000165,"versionName":"8.5.3","isHomeApp":false},{"package":"com.xyskkj.garderobe","activity":"com.xyskkj.garderobe.activity.WelcomeActivity","appLabel":"�����³�","versionCode":759,"versionName":"7.5.9","isHomeApp":false}],"filename":""})
```

adb connect 127.0.0.1:5555
appium inspector����ʹ�ý̳̲ο����ӣ� https://blog.csdn.net/YZL40514131/article/details/129632934?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-129632934-blog-130526178.235^v39^pc_relevant_anti_vip_base&spm=1001.2101.3001.4242.2&utm_relevant_index=2






















































