# appium

appium git项目仓库： https://github.com/appium/appium
官网：https://appium.io/

# 使用快速开始
1. 安装 appium: 下载地址为 https://appium.io/docs/en/2.3/quickstart/install/
   系统配置要求：
   1） macOS/Linux/Windows
   2) Node.js  version >= 18.0.0 
   3) npm version >= 8 
   4)By itself, Appium is relatively lightweight and doesn't have significant disk space or RAM requirements. It can even be run in resource-constrained environments like Raspberry Pi, so long as Node.js is available.
    就其本身而言，Appium相对较轻，没有显著的磁盘空间或RAM需求。只要Node.js可用，它甚至可以在资源受限的环境中运行，如Raspberry Pi。
   安装命令：
    1） npm i -g appium  
   试用：
    准备环境：
      1） Windows 11
      2） Node.js version==18.16.1 (node -v)
      3)  npm version==9.5.1 (npm --version)
    在命令行执行命令安装appium：npm i -g appium 
    安装成功后， 在命令行执行: appium  （我执行的时候， appium version==v2.3.0）
    执行完运行命令后，如果看到： [Appium] Welcome to Appium v2.0.0  （代表启动成功， appium正在运行）
2. 安装 UiAutomator2 Driver  （git地址： https://github.com/appium/appium-uiautomator2-driver）
   1)查看appium git仓库的readme.md 可以知道3中安装driver的方法
        1） npm安装： appium driver install --source=npm appium-xcuitest-driver[@<version>]  实际命令：npm install -g appium-xcuitest-driver@2.3.0   安装成功
        2) 本地安装
        3） github安装: appium driver install uiautomator2
2.1 C:\Users>appium driver list
√ Listing available drivers
- uiautomator2@2.35.0 [installed (npm)]
- xcuitest [not installed]
- mac2 [not installed]
- espresso [not installed]
- safari [not installed]
- gecko [not installed]
- chromium [not installed]
- 
3. 安装 安卓sdk
   ) ANDROID_HOME
4. appium的启动命令：appium server --address 192.168.56.1:4723   --allow-cors

4. 写自己的测试脚本, 可选的脚本语言有
   1） js
   2) java 
   3) python (我选择用python， 提供的示例：https://appium.io/docs/en/2.3/quickstart/test-py/)
   4) ruby
   5) .net c# 
   
   python appium脚本步骤：
       1）安装python appium脚本依赖库： pip install Appium-Python-Client 
       
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
   遇到的问题：
   1. java环境得要要16+， 否则报错： devices一直offline 
5. 自己实现demo， 以研究安卓手机上的富途牛牛为例子：
   查找app的包名：
   1. adb shell pm list packages 通过pc端cmd的adb命令，查出手机中所有的app的包名 
   2. adb shell pm list packages | findstr futu  查出富途的包名， futu是自己猜测包中名称会含有的字眼
   查找app的Activity（已安装的apk的查找方法, 参考链接： https://blog.csdn.net/gaogsf/article/details/124472026） 
   
   1. 将安装有app的手机连接到到电脑上，运行adb devices,显示设备
   2. cmd命令行：adb shell logcat > D:/log.log，运行  
   3. 手机上打开app应用
   4. Ctrl c 关闭adb logcat命令行
   5. 打开log.log文件，搜索关键字，查出自己研究的app的MainActivity或者LaunchActivity 
   搜索和分析的关键字根据具体情况有以下几种， 主要是找到启动应用程序标志：
   ```python
   搜索： .LaunchActivity
   
    12-25 14:52:52.773  1459  1495 I StatusBarDisable: setFlags what=0 which=1 pkg=Window{b4fdd53 u0 cn.futu.trader/cn.futu.trader.launch.activity.LaunchActivity}
    12-25 14:52:52.776  1459  1505 I ActivityManager: Displayed cn.futu.trader/.launch.activity.LaunchActivity: +1s195ms
        搜索： .MainActivity
    12-25 14:53:15.642  1459  1865 I ActivityManager: START u0 {act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 hwFlg=0x10 cmp=com.cmschina.cmschina_hk_app/.MainActivity bnds=[855,1018][1065,1325]} from uid 10060
    12-25 14:53:15.643  1459  1865 I ActivityManager: ActivityRecord info: ActivityInfo{85c4298 com.cmschina.cmschina_hk_app.MainActivity}
   
    12-25 17:53:53.209  1967  1999 I HCALL   : hcallSyncInstalledAppsRpc({"apps":[{"package":"io.appium.settings","activity":"io.appium.settings.Settings","appLabel":"Appium Settings","versionCode":62,"versionName":"5.2.0","isHomeApp":false},{"package":"com.cmschina.cmschina_hk_app","activity":"com.cmschina.cmschina_hk_app.MainActivity","appLabel":"招商证券国际","versionCode":399,"versionName":"3.0.0","isHomeApp":false},{"package":"cn.damai","activity":"cn.damai.launcher.splash.SplashMainActivity","appLabel":"大麦","versionCode":6000165,"versionName":"8.5.3","isHomeApp":false},{"package":"com.xyskkj.garderobe","activity":"com.xyskkj.garderobe.activity.WelcomeActivity","appLabel":"极简衣橱","versionCode":759,"versionName":"7.5.9","isHomeApp":false}],"filename":""})
```

adb connect 127.0.0.1:5555
appium inspector工具使用教程参考链接： https://blog.csdn.net/YZL40514131/article/details/129632934?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-129632934-blog-130526178.235^v39^pc_relevant_anti_vip_base&spm=1001.2101.3001.4242.2&utm_relevant_index=2






















































