# 安卓app逆向（以第一证券app为例）


#  fiddler抓包
由于第一证券，试过抓包， 但是没有抓到有效的包， 这个方式在第一证券app中，没有起到大作用.


# app逆向
本质是分析app， 人在app上做的操作， 用代码实现。
apk-》 安卓开发-》 java代码写-》 看得懂会分析java代码。 

# 反编译工具：
静态分析，学习jadx反编译
apk文件， 本质是压缩包（代码）
反编译工具： 反编译成功java代码， 分析java代码， 例如： jadx（目前是使用这个， 其它的试过了apktool用起来效果和jadx，后面就直接用jadx了）, apktool, jeb， jda
反编译工具都依赖jre（java开发环境）， jadx可以直接下载带jre环境的版本。 


# 第一证券app， 目前找到比较有点效果的一个逆向方法
   1、frida hook逆向
   2、使用 Frida Gadget（虽然可以不用root手机， 但是需要打包到目标apk中， 这个不适用当前场景。） 


# 准备工具环境：
1. 模拟器： 雷电， 官网： https://www.ldmnq.com/?n=6000
2. 安卓sdk： adb 官网：https://developer.android.com/tools/adb?hl=zh-cn
3. python: 安装frida-tools库
4. jadx: https://github.com/skylot/jadx/releases/tag/v1.4.7
5. frida-server: 


# 获取apk
1. 官网下载
2. google play 商店下载安装到手机或者模拟器， 用adb获取下载apk。 

#  用jadx工具， 打开 第一证券.apk , 查看代码  

# python端安装frida-tools工具
## 配置 frida-server 环境 
### 配置 frida-server 环境 
pip install frida-tools -i https://pypi.tuna.tsinghua.edu.cn/simple
会一快安装两个库： 
frida-tools:  12.4.2
frida:  16.2.5版本。 (后面下载frida-server得要下载这个版本， 否则会不匹配。)
可能会报下面的错误： 
Unable to save SELinux policy to the kernel: Permission denied
Unable to start: Error binding to address 127.0.0.1:27042: Address already in use

python 客户端运行，可能会报下面的错误:
session = device.attach('com.firstsechk.tc.trade')
session = device.attach(3644)
frida.PermissionDeniedError: unable to access process with pid 3644
Failed to attach to target app1: unable to perform ptrace getregs: Device or resource busy


### 模拟器端-安卓机端： 安装frida-server服务器，启动frida-server。
安卓手机查看cpu架构： adb shell getprop ro.product.cpu.abi
三星Galaxy A 71结果： arm64-v8a  (后面因为要root手机，所以还是得用模拟器)
更详细的信息： adb shell cat /proc/cpuinfo

#### 查看雷电模拟器中的android的cpu：
adb shell getprop ro.product.cpu.abi
结果： x86_64
下载相对应版本的frida-server ： frida-server-16.2.5-android-x86_64 并解压。 
frida安装在安卓设备上的frida-server下载地址： https://github.com/frida/frida/releases

#### 准备安卓中得frida-server环境;
将 frida-server 文件复制到安卓设备上。你可以使用 adb 命令将文件复制到设备的 /data/local/tmp/ 目录中
adb push frida-server-16.2.5-android-x86_64 /data/local/tmp
adb -s emulator-5554 push adb push D:\WorkData\bot_first_trade_app_api\package\frida-server-16.2.5-android-x86_64 /data/local/tmp /data/local/tmp/

adb -s emulator-5554 shell
su root
cd /data/local/tmp
cp frida-server-16.2.5-android-x86_64  frida-server
chmod 777 frida-server
./frida-server


查看frida-server进程：
adb shell top:
3894 shell        20   0 187M  16M 2.7M S  0.0   0.4   0:00.33 frida-server
停止进程: kill 3894 

端口转发：
adb -s emulator-5554 forward tcp:27042 tcp:27042
移除端口转发规则： adb forward --remove-all

# frida hook 
   使用frida 进行hook, 通过一边编写hook，一边分析堆栈信息

# 参考链接：
1. frida安装以及简单使用： https://blog.csdn.net/XBXX_java/article/details/128862595
2. 安卓逆向 - 基础入门教程https://blog.csdn.net/weixin_42840266/article/details/132080000
3. frida hook的教程：  https://blog.csdn.net/weixin_42840266/article/details/132279975 （起到作用）
4. frida快速入门教程: https://www.bilibili.com/video/BV1m84y1D7gh/?spm_id_from=333.337.search-card.all.click&vd_source=9ab8a945335cbaf24c13e51eba88b195
