下载资源清单：
模拟器： 雷电， 官网： https://www.ldmnq.com/?n=6000
安卓sdk： adb 官网：https://developer.android.com/tools/adb?hl=zh-cn
apktool: https://apktool.org/
安卓工具网：https://www.androiddevtools.cn/
python：安装frida-tools库
jadx: https://github.com/skylot/jadx/releases/tag/v1.4.7






https://github.com/ctfs/write-ups-2015/tree/master/seccon-quals-ctf-2015/binary/reverse-engineering-android-apk-1
frida安装在安卓手机上的frida服务器apk下载地址： https://github.com/frida/frida/releases
博客教程-frida安装以及简单使用： https://blog.csdn.net/XBXX_java/article/details/128862595

frida-server的下载： 最新版本没有看到frida-server, 往之前的版本翻， 16.0.16版本看到了
后面发现是自己没有打开，16.2.5版本就有frida-server。 

将 frida-server 文件复制到安卓设备上。你可以使用 adb 命令将文件复制到设备的 /data/local/tmp/ 目录中
adb push frida-server-16.0.16-android-arm64 /data/local/tmp/
adb -s 192.168.5.3:5555 push E:\my_codes\all_demos\python_modules\modules_spider\md_spider_awesome\md_frida_tools\packages\frida-server-16.2.5-android-arm64 /data/local/tmp/
adb -s 192.168.5.3:5555 push E:\my_codes\all_demos\python_modules\modules_spider\md_spider_awesome\md_frida_tools\packages\frida-server-16.2.5-android-x86_64 /data/local/tmp/


建议重命名为: frida-server
C:\Users\fxxji>adb push frida-server /data/local/tmp
frida-server: 1 file pushed, 0 skipped. 79.4 MB/s (52432024 bytes in 0.630s)

这个得要root手机， 真机不方便root。 
使用 Frida Gadget， 虽然可以不用root手机， 但是需要打包到目标apk中， 这个不适用场景。 
需要改为模拟使用。 


Unable to save SELinux policy to the kernel: Permission denied
Unable to start: Error binding to address 127.0.0.1:27042: Address already in use


查看frida-server进程：
top:
3894 shell        20   0 187M  16M 2.7M S  0.0   0.4   0:00.33 frida-server

停止进程: kill 3894 


https://www.cnblogs.com/wutou/p/17892368.html

端口转发： 

adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

移除端口转发规则： adb forward --remove-all


错误信息:
session = device.attach('com.firstsechk.tc.trade')
session = device.attach(3644)
frida.PermissionDeniedError: unable to access process with pid 3644

 
Failed to attach to target app1: unable to perform ptrace getregs: Device or resource busy




frida hook:
hook的教程：  https://blog.csdn.net/weixin_42840266/article/details/132279975 （起到关键作用，研究有突破）


hook内容:
java.net.URL
结果： 
[*] Attached to target app: 第一证券(香港)
加密前：http://mtrade.afe.com.hk/mobile/secureNewsHeadline.aspx?seckey=18239&max=50&categoryid=61
{'type': 'error', 'description': "ReferenceError: 'showStacks' is not defined", 'stack': "ReferenceError: 'showStacks' is not defined\n    at <anonymous> (/script1.js:8)\n    at apply (native)\n    at ne (frida/node_modules/frida-java-bridge/lib/class-factory.js:677)\n    at <anonymous> (frida/node_modules/frida-java-bridge/lib/class-factory.js:655)", 'fileName': 
'/script1.js', 'lineNumber': 8, 'columnNumber': 1}



加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
{'type': 'error', 'description': "ReferenceError: 'showStacks' is not defined", 'stack': "ReferenceError: 'showStacks' is not defined\n    at <anonymous> (/script1.js:8)\n    at apply (native)\n    at ne (frida/node_modules/frida-java-bridge/lib/class-factory.js:677)\n    at <anonymous> (frida/node_modules/frida-java-bridge/lib/class-factory.js:655)", 'fileName': 
'/script1.js', 'lineNumber': 8, 'columnNumber': 1}



设备上运行的进程104:Process(pid=15598, name="第一证券(香港)", parameters={})
[*] Attached to target app: com.firstsechk.tc.trade
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
加密前：http://m.afe.com.hk/iphone/disclaimer.asp?package=-2147483648
加密前：http://m.afe.com.hk/iphone/disclaimer.asp?package=-2147483648
加密前：http://m.afe.com.hk/iphone/disclaimer.asp?package=-2147483648
加密前：http://m.afe.com.hk/iphone/disclaimer.asp?package=-2147483648
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
加密前：http://m.afe.com.hk/iphone/disclaimer.asp?package=-2147483648




[*] Attached to target app: com.firstsechk.tc.trade
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
java.lang.Exception
        at java.net.URL.<init>(Native Method)
        at o5.e.d(SourceFile:30)
        at b1.c.e(SourceFile:11)
        at com.afe.mobilecore.AppCoreDelegate.p(SourceFile:532)
        at com.afe.mobilecore.AppCoreDelegate.J(SourceFile:2239)
        at k1.v.c(Unknown Source:50)
        at j1.b.j1(Unknown Source:8)
        at f.x.run(SourceFile:948)
        at java.lang.Thread.run(Thread.java:764)

加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
java.lang.Exception
        at java.net.URL.<init>(Native Method)
        at com.android.okhttp.HttpUrl.url(HttpUrl.java:327)
        at com.android.okhttp.Request.url(Request.java:53)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.execute(HttpURLConnectionImpl.java:463)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.connect(HttpURLConnectionImpl.java:132)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.getOutputStream(HttpURLConnectionImpl.java:263)
        at o5.c.run(SourceFile:23)



[*] Attached to target app: com.firstsechk.tc.trade
key : sound_effects_enabled
val : 1
param>> a:771589S, b:Gr89LM, c:null, d: null, e: 19, f：F






参数列表:
设备上运行的进程102:Process(pid=15329, name="com.android.webview:webview_service", parameters={})
设备上运行的进程103:Process(pid=16073, name="com.firstsechk.tc.trade", parameters={})
设备上运行的进程104:Process(pid=16162, name="第一证券(香港)", parameters={})
[*] Attached to target app: com.firstsechk.tc.trade
key : sound_effects_enabled
val : 1
param>> a:771589S, b:Gr89LM, c:null, d: null, e: 19, f：F
key : java.util.concurrent.ThreadPoolExecutor$Worker@4ddc13a[State = -1, empty queue]
val : java.lang.Object@2721eb
key : java.util.concurrent.ThreadPoolExecutor$Worker@3c13b48[State = -1, empty queue]
val : java.lang.Object@2721eb
key : 
val : :  0.0  1.0
key :
val : :  0.0  1.0
key : android.animation.AnimatorSet$Node@ba9f71d
val : android.animation.AnimatorSet$Node@e173d92
key : trimPathStart
val : trimPathStart:  0.0  0.75
key : android.animation.AnimatorSet$Node@d22b60
val : android.animation.AnimatorSet$Node@ef3e819
key : trimPathEnd
val : trimPathEnd:  0.0  0.75  
key : android.animation.AnimatorSet$Node@15752bf
val : android.animation.AnimatorSet$Node@c1e9d8c
key : trimPathOffset
val : trimPathOffset:  0.0  0.25
key : android.animation.AnimatorSet$Node@1c8ecea
val : android.animation.AnimatorSet$Node@1b85bdb
key : rotation
val : rotation:  0.0  720.0
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
java.lang.Exception
        at java.net.URL.<init>(Native Method)
        at o5.e.d(SourceFile:30)
        at b1.c.e(SourceFile:11)
        at b1.c.e(Native Method)
        at com.afe.mobilecore.AppCoreDelegate.p(SourceFile:532)
        at com.afe.mobilecore.AppCoreDelegate.J(SourceFile:2239)
        at k1.v.c(Unknown Source:50)
        at j1.b.j1(Unknown Source:8)
        at f.x.run(SourceFile:948)
        at java.lang.Thread.run(Thread.java:764)

result begin
true
result end
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
java.lang.Exception
        at java.net.URL.<init>(Native Method)
        at com.android.okhttp.HttpUrl.url(HttpUrl.java:327)
        at com.android.okhttp.Request.url(Request.java:53)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.execute(HttpURLConnectionImpl.java:463)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.connect(HttpURLConnectionImpl.java:132)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.getOutputStream(HttpURLConnectionImpl.java:263)
        at o5.c.run(SourceFile:23)

key : java.net.AddressCache$AddressCacheKey@431ade92
val : java.net.AddressCache$AddressCacheEntry@6dbe18d
key : http://trade.firstsechk.com
val : [JSESSIONID=2F51C2227579E389FEDC02773CE0410E]
key : SMS_NUM
val : [B@a662f42
key : OTP_LOGIN_FLAG
val : [B@bf72c90
key : OTP_CHG_PWD_FLAG
val : [B@2bfd8e
key : WAIT_TIME
val : [B@c4a81bc
key : TELNO_OFFICE
val : [B@16e649a
key : ENABLE_GREY_MKT
val : [B@1bfda8
key : GREY_MKT_AVAIL_LIST
val : [B@a3e3066
key : GREY_MKT_ALLOW_AMEND_LIST
val : [B@d074c54
key : GREY_MKT_BLK_LIST
val : [B@4ececf2
key : ENCRYPT_METHOD
val : [B@4b6d9c0
key : RETURN_STATUS
val : [B@d58e63e
key : RETURN_ERROR_MSG
val : [B@70fd1ec
key : RETURN_ERROR_CODE
val : [B@cf9284a
key : 330813bf-4162-4d3f-9910-7a63201bed9f
val : androidx.fragment.app.m1@ced2a6d
key : androidx.activity.OnBackPressedDispatcher$LifecycleOnBackPressedCancellable@13676a2
val : androidx.activity.OnBackPressedDispatcher$LifecycleOnBackPressedCancellable@13676a2=androidx.lifecycle.s@fa20f33
key : 330813bf-4162-4d3f-9910-7a63201bed9f
val : FragmentManagerViewModel{d1432f0} Fragments () Child Non Config () ViewModelStores ()
key : 941670626
val : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:StartActivityForResult
key : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:StartActivityForResult
val : 941670626
key : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:StartActivityForResult
val : androidx.activity.result.f@ebf0069
key : 826399979
val : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:StartIntentSenderForResult
key : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:StartIntentSenderForResult
val : 826399979
key : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:StartIntentSenderForResult
val : androidx.activity.result.f@3a95aee
key : 1959146287
val : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:RequestPermissions
key : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:RequestPermissions
val : 1959146287
key : FragmentManager:330813bf-4162-4d3f-9910-7a63201bed9f:RequestPermissions
val : androidx.activity.result.f@ae46b8f
key : androidx.fragment.app.Fragment$5@ba18e1c
val : androidx.fragment.app.Fragment$5@ba18e1c=androidx.lifecycle.s@2be3a25
key : androidx.savedstate.Recreator@e5437fa
val : androidx.savedstate.Recreator@e5437fa=androidx.lifecycle.s@84631ab
key : androidx.savedstate.SavedStateRegistry$1@e477008
val : androidx.savedstate.SavedStateRegistry$1@e477008=androidx.lifecycle.s@6bd53a1
key : 330813bf-4162-4d3f-9910-7a63201bed9f
val : androidx.lifecycle.q0@93a88dd
key :
val : :  0.0  1.0
key : androidx.savedstate.Recreator@4aaf695
val : androidx.savedstate.Recreator@4aaf695=androidx.lifecycle.s@2a93aa
key : androidx.savedstate.SavedStateRegistry$1@a9adb9b
val : androidx.savedstate.SavedStateRegistry$1@a9adb9b=androidx.lifecycle.s@7baeb38
key : androidx.fragment.app.l@8fdee02
val : java.lang.Object@2721eb
key : y.b@a2f2313
val : java.lang.Object@2721eb
key : y.b@673e950
val : java.lang.Object@2721eb
key : Operation {450e749} {mFinalState = VISIBLE} {mLifecycleImpact = ADDING} {mFragment = v{a764076} (330813bf-4162-4d3f-9910-7a63201bed9f id=0x7f0901f0)}
val : false
