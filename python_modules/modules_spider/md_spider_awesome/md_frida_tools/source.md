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






又hook了 [o5.e.d]
结果：

错误的账号密码：
[*] Attached to target app: com.firstsechk.tc.trade
param>> a:123456w, b:1234545, c:null, d: null, e: 25, f：F
[o5.e.d] param>> a:1, b:0, c:http://trade.firstsechk.com/i-trade/streaming/streamLogin, d: re=1&clm=eg%2F3FgiFfK4ajtPDmNPk8XJquqMkpdp%2FE9ZRHlVNjKy0ecOG4%2B83pZSm5QjVRXss51P%2BMmFSGLhP%0AUCry61teZdGo8qWz5G5hCA6gD3ElsTtgwifN38epMNtcxyWZnd4VccxLybZFDJKPeKvKYiVkk9Sh%0Av%2Fvs0G%2FV8chb1Y3UxhkFSYtZpalrw2kA3%2FniPMbI%2BUGw5p5BBS3mTSy10fD84J0tFyxARlmbC%2Bpx%0AcIch9Fe%2BvtXjzhixPy57romQm5N0xU%2FZ9igVzbFfp618ciMdOWoV7ZanWiGg%2FZcCmqOHClep6153%0AHSEFHOnUoFMp0lYPAJwM10i2es6rU%2B0Vn9WBJBFcXCjPNne3NJcqeCq%2BIQcWlVQZHbPAoi3cG4vD%0Axf9hjMfd2Lau5a6PCj2nJeqe%2Bqd5Gh4V42hT3jb7AbPv1mBvlnJtY3ahwLFQz14Lt1QN%2B4q6qlFq%0AI7zXdBgNtRYozO9BpnvLUDpsQSK1ViC5fvjmDpWtEm%2B9cyNU2nuC7f9ceH9U9RCnGN%2Bn5u1ZI0sI%0AQWV6PrnFNIWZ6mX7p%2FqDwXXbzk0tCxSe7ikWDD38IxuvpGdF8egskxE7pgUa7w7zrzwrIhfptBgJ%0A9F9muIvlBqtP9b4LG4AtXsIAaXb0ty0IFPB1gnAmuz3D97xj35w%2F9m3kQEhV594ymJZ2hWm6wKs%3D%0A
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
java.lang.Exception
        at java.net.URL.<init>(Native Method)
        at o5.e.d(SourceFile:30)
        at o5.e.d(Native Method)
        at b1.c.e(SourceFile:11)
        at b1.c.e(Native Method)
        at com.afe.mobilecore.AppCoreDelegate.p(SourceFile:532)
        at com.afe.mobilecore.AppCoreDelegate.J(SourceFile:2239)
        at k1.v.c(Unknown Source:50)
        at j1.b.j1(Unknown Source:8)
        at f.x.run(SourceFile:948)
        at java.lang.Thread.run(Thread.java:764)

result begin
303
result end
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
java.lang.Exception
        at o5.e.d(Native Method)
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
java.lang.Exception
        at b1.c.e(Native Method)
        at com.afe.mobilecore.AppCoreDelegate.p(SourceFile:532)
        at com.afe.mobilecore.AppCoreDelegate.J(SourceFile:2239)
        at k1.v.c(Unknown Source:50)
        at j1.b.j1(Unknown Source:8)
        at f.x.run(SourceFile:948)
        at java.lang.Thread.run(Thread.java:764)

java.lang.Exception
        at java.net.URL.<init>(Native Method)
        at com.android.okhttp.HttpUrl.url(HttpUrl.java:327)
        at com.android.okhttp.Request.url(Request.java:53)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.execute(HttpURLConnectionImpl.java:463)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.connect(HttpURLConnectionImpl.java:132)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.getOutputStream(HttpURLConnectionImpl.java:263)
        at o5.c.run(SourceFile:23)


正确的账号密码：

[o5.e.d] param>> a:1, b:0, c:http://trade.firstsechk.com/i-trade/streaming/streamLogin, d: re=1&clm=r7cVKRuhJyjF2LNgk%2F0tC%2BI2kJheMBxx%2BTrR4dLUGbVYUiyXldMZUM2AF2NwO7Nutn2N8sG0c%2Fwf%0A23Z%2BW9NC8pkiIWqiMJkqEaAkMuqVaatx5mBYTugp4p75%2Fwe9q%2BTFDdjuQTXPqn9ZoQBomSwsKxs8%0AKbEIJmHNBmSmoNQrAZ8Q32wq%2FVfbXDbjaXghQjIr%2B%2Fk3KEfunkx58BMQl5WLVeuufmvkcUX3uqxi%0Ar7b2vMIGj287FmpiI2adsqLZzpXEc7MpK8uD6JkmTCeNsQ2kXgm5I2up2YkCE7eq%2B1MZz4YN4O5p%0Ay%2FHsPmxVgkOSF2Q5XFgNlK0Vl%2FPLHN49YN4UHJ163eS%2BIg3U41bzcfYGSe5HMpDoo14qol5b9w7F%0AFkfMNZfX2fFhMjhnKR3XQSUD%2F3ihup9lRf9dL6ZQUW2KGkcNNagQV%2Bmi7Dgg6fWJez5jTXoYRkDz%0AfzM%2FJweTRhBINSLL2o7bVU7PhpB4im9q1yYluK3SAecyTBhWhhA9NtpVPgkaa2FqBs7vKEXUpkio%0AnO5AWUK9MQriF9uItOfrr%2F49vTMCjDaJ1ndgDD59E9TxCGQ0bEiohxbEV5mqeyXcYsNsLP3zsr%2FV%0ACb8YCE1Lth9xgdW%2BApgKm5nS0W3lC4J7YdhPutIxXRUqdJDTt17rYdFmj28CgdMSCPvpRy99KgU%3D%0A
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
java.lang.Exception
        at java.net.URL.<init>(Native Method)
        at o5.e.d(SourceFile:30)
        at o5.e.d(Native Method)
        at b1.c.e(SourceFile:11)
        at b1.c.e(Native Method)
        at com.afe.mobilecore.AppCoreDelegate.p(SourceFile:532)
        at com.afe.mobilecore.AppCoreDelegate.J(SourceFile:2239)
        at k1.v.c(Unknown Source:50)
        at j1.b.j1(Unknown Source:8)
        at f.x.run(SourceFile:948)
        at java.lang.Thread.run(Thread.java:764)

result begin
261
result end
加密前：http://trade.firstsechk.com/i-trade/streaming/streamLogin
java.lang.Exception
        at o5.e.d(Native Method)
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
java.lang.Exception
        at b1.c.e(Native Method)
        at com.afe.mobilecore.AppCoreDelegate.p(SourceFile:532)
        at com.afe.mobilecore.AppCoreDelegate.J(SourceFile:2239)
        at k1.v.c(Unknown Source:50)
        at j1.b.j1(Unknown Source:8)
        at f.x.run(SourceFile:948)
        at java.lang.Thread.run(Thread.java:764)

java.lang.Exception
        at java.net.URL.<init>(Native Method)
        at com.android.okhttp.HttpUrl.url(HttpUrl.java:327)
        at com.android.okhttp.Request.url(Request.java:53)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.execute(HttpURLConnectionImpl.java:463)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.connect(HttpURLConnectionImpl.java:132)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.getOutputStream(HttpURLConnectionImpl.java:263)
        at o5.c.run(SourceFile:23)

key : java.net.AddressCache$AddressCacheKey@431ade92
val : java.net.AddressCache$AddressCacheEntry@2bfd8e
key : java.net.CookieManager
val : java.lang.ref.WeakReference@3d069af
key : http://trade.firstsechk.com
val : [JSESSIONID=A8A460F4DBCC2FB0D63D6562C047908F]
key : SMS_NUM
val : [B@c4a81bc
key : OTP_LOGIN_FLAG
val : [B@16e649a
key : OTP_CHG_PWD_FLAG
val : [B@1bfda8
key : WAIT_TIME
val : [B@a3e3066
key : TELNO_OFFICE
val : [B@d074c54
key : ENABLE_GREY_MKT
val : [B@4ececf2
key : GREY_MKT_AVAIL_LIST
val : [B@4b6d9c0
key : GREY_MKT_ALLOW_AMEND_LIST
val : [B@d58e63e
key : GREY_MKT_BLK_LIST
val : [B@70fd1ec
key : ENCRYPT_METHOD
val : [B@cf9284a
key : RETURN_STATUS
val : [B@b1e20d8
key : RETURN_ERROR_MSG
val : [B@ba97f16
key : RETURN_ERROR_CODE
val : [B@ac07284
key : ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b
val : androidx.fragment.app.m1@ae46b8f
key : androidx.activity.OnBackPressedDispatcher$LifecycleOnBackPressedCancellable@ba18e1c
val : androidx.activity.OnBackPressedDispatcher$LifecycleOnBackPressedCancellable@ba18e1c=androidx.lifecycle.s@2be3a25
key : ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b
val : FragmentManagerViewModel{e5437fa} Fragments () Child Non Config () ViewModelStores ()
key : 163186847
val : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:StartActivityForResult
key : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:StartActivityForResult
val : 163186847
key : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:StartActivityForResult
val : androidx.activity.result.f@84631ab
key : 61907145
val : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:StartIntentSenderForResult
key : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:StartIntentSenderForResult
val : 61907145
key : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:StartIntentSenderForResult
val : androidx.activity.result.f@e477008
key : 1661230620
val : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:RequestPermissions
key : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:RequestPermissions
val : 1661230620
key : FragmentManager:ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b:RequestPermissions
val : androidx.activity.result.f@6bd53a1
key : androidx.fragment.app.Fragment$5@d9dd9c6
val : androidx.fragment.app.Fragment$5@d9dd9c6=androidx.lifecycle.s@9b43d87
key : androidx.savedstate.Recreator@9e784b4
val : androidx.savedstate.Recreator@9e784b4=androidx.lifecycle.s@93a88dd
key : androidx.savedstate.SavedStateRegistry$1@b8dcc52
val : androidx.savedstate.SavedStateRegistry$1@b8dcc52=androidx.lifecycle.s@90d2b23
key : ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b
val : androidx.lifecycle.q0@57d567f
key :
val : :  0.0  1.0
key : androidx.savedstate.Recreator@d419677
val : androidx.savedstate.Recreator@d419677=androidx.lifecycle.s@7cf82e4
key : androidx.savedstate.SavedStateRegistry$1@d94634d
val : androidx.savedstate.SavedStateRegistry$1@d94634d=androidx.lifecycle.s@8fdee02
key : androidx.fragment.app.l@cb64a7c
val : java.lang.Object@f56b706
key : y.b@c37af05
val : java.lang.Object@f56b706
key : y.b@de73b5a
val : java.lang.Object@f56b706
key : Operation {125e18b} {mFinalState = VISIBLE} {mLifecycleImpact = ADDING} {mFragment = v{673e950} (ce5527eb-3eb6-4a4d-b6c9-80d2ec890a8b id=0x7f0901f0)}
val : false
