#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/24 14:24
# @File     : firsttrade_frida_hook_demo_one.py
# @Desc     :
import frida
import sys

DEVICE_UID = 'emulator-5554'


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


def main(process_matches):
    # 连接到本地 Frida 服务器
    try:
        device = frida.get_device(DEVICE_UID)
    except Exception as e:
        print("Failed to connect to USB device:", e)
        sys.exit(1)

    print("[*] Connected to USB device:", device)

    target_name = ''
    # 启动 Frida 客户端
    try:
        processes = device.enumerate_processes()
        found = False
        for i, process in enumerate(processes):
            print(f'设备上运行的进程{i+1}:{process}')
            if not found:
                for match in process_matches:
                    if process.name.find(match) != -1:
                        target_name = process.name
                        found = True 
    except Exception as e:
        print("Failed to enumerate_processes:", e)
        sys.exit(1)

    if not target_name:
        print('找不到对应的进程: ', process_matches)
        return

    # 启动 Frida 客户端
    try:
        session = device.attach(target_name)
    except Exception as e:
        print("Failed to attach to target app:", e)
        sys.exit(1)

    print("[*] Attached to target app:", target_name)

    # 在目标进程中注入脚本
    js = """
  Java.perform(() => {
  // Function to hook is defined here
  const MainActivity = Java.use('com.afe.mobilecore.tcuicore.RootBaseActivity');
                     
  const keys = Object.keys(MainActivity);
  send('Object.keys(MainActivity): ')                      
  send(keys);

  // Whenever button is clicked
  const onClick = MainActivity.onClick;
  onClick.implementation = function (v) {
    // Show a message to know that the function got called
    send('onClick');

    // Call the original onClick handler
    onClick.call(this, v);

    // Set our values after running the original onClick handler
    this.m.value = 0;
    this.n.value = 1;
    this.cnt.value = 999;

    // Log to the console that it's done, and we should have the flag!
    console.log('Done:' + JSON.stringify(this.cnt));
  };
});
    """
    js = """
        Java.perform(() => {
        // Function to hook is defined here
        const MainActivity = Java.use('com.afe.mobilecore.tcuicore.RootBaseActivity');
        send('demo');
        //MainActivity.$init.implementation = function () {
        //    send('MainActivity.init...');
        //    return this.$init();
        //};
        });

    """

    # hook OnClick方法
    js = """
    Java.perform(function() {
    // Helper function to hook methods
    function hookOnClickMethods(className) {
        var clazz = Java.use(className);
        clazz.onClick.implementation = function(view) {
            console.log('onClick called in class: ' + className);
            console.log('View: ' + view.toString());
            this.onClick(view);  // Call the original method
        };
    }

    // List of common classes implementing OnClickListener
    var commonOnClickListeners = [
        'android.view.View$OnClickListener'
    ];

    // Hook all classes implementing OnClickListener
    Java.enumerateLoadedClasses({
        onMatch: function(className) {
            // send('ClassName: ' + className);
            try {
                if (className.indexOf('ClickListener') != -1) {
                    // send('ClickClassName: ' + className)
                    hookOnClickMethods(className);
                }

                var clazz = Java.use(className);
                if (Java.cast(clazz, Java.use('android.view.View$OnClickListener'))) {
                    hookOnClickMethods(className);
                }
            } catch (e) {
                // Ignore errors
            }
        },
        onComplete: function() {
            console.log('Completed hooking OnClick methods');
        }
    });

    // Hook classes loaded in the future
    var classLoader = Java.classFactory.loader;
    classLoader.hook('loadClass', function(target, method, thisObject, args) {
        var className = args[0];
        var clazz = null;
        try {
            if (className.indexOf('ClickListener') != -1) {
                send('ClickClassName: ' + className);
                hookOnClickMethods(className);
            }
            clazz = Java.use(className);
            if (Java.cast(clazz, Java.use('android.view.View$OnClickListener'))) {
                hookOnClickMethods(className);
            }
        } catch (e) {
            // Ignore errors
        }
    });

    // Additional specific hooks (if needed)
    commonOnClickListeners.forEach(hookOnClickMethods);
});

"""

    # hook网络请求
    js = """
    Java.perform(function() {
    // Helper function to safely hook methods
    function tryHook(className, method, hookFunction) {
        try {
            var clazz = Java.use(className);
            var overloads = clazz[method].overloads;
            overloads.forEach(function(overload) {
                overload.implementation = hookFunction;
            });
            console.log("Successfully hooked " + className + "." + method);
        } catch (e) {
            console.error("Failed to hook " + className + "." + method + ": " + e.message);
        }
    }

    // Hook OkHttpClient
    tryHook('okhttp3.OkHttpClient', 'newCall', function(request) {
        console.log('OkHttp Request: ' + request.toString());
        var response = this.newCall(request);
        return response;
    });

    // Hook HttpURLConnection
    try {
        var HttpURLConnection = Java.use('java.net.HttpURLConnection');

        HttpURLConnection.getOutputStream.implementation = function() {
            console.log('HttpURLConnection Request URL: ' + this.getURL().toString());
            return this.getOutputStream();
        };

        HttpURLConnection.getInputStream.implementation = function() {
            console.log('HttpURLConnection Response URL: ' + this.getURL().toString());
            return this.getInputStream();
        };
    } catch (e) {
        console.error("Failed to hook HttpURLConnection: " + e.message);
    }

    // Hook Retrofit
    try {
        var RetrofitBuilder = Java.use('retrofit2.Retrofit$Builder');
        RetrofitBuilder.build.implementation = function() {
            var retrofit = this.build();
            var httpClient = retrofit.callFactory();
            console.log('Retrofit instance created with httpClient: ' + httpClient);
            return retrofit;
        };

        var OkHttpCall = Java.use('retrofit2.OkHttpCall');
        OkHttpCall.execute.implementation = function() {
            console.log('Retrofit Request: ' + this.request().toString());
            var response = this.execute();
            console.log('Retrofit Response: ' + response.toString());
            return response;
        };

        OkHttpCall.enqueue.implementation = function(callback) {
            console.log('Retrofit Request: ' + this.request().toString());
            this.enqueue(callback);
        };
    } catch (e) {
        console.error("Failed to hook Retrofit: " + e.message);
    }

    // Hook Volley
    try {
        var Request = Java.use('com.android.volley.Request');
        Request.toString.implementation = function() {
            console.log('Volley Request: ' + this.getUrl());
            return this.toString();
        };

        var NetworkDispatcher = Java.use('com.android.volley.NetworkDispatcher');
        NetworkDispatcher.processRequest.implementation = function(request) {
            console.log('Volley Request: ' + request.getUrl());
            this.processRequest(request);
        };
    } catch (e) {
        console.error("Failed to hook Volley: " + e.message);
    }
});


"""


    js = """
        Java.perform(() => {
        // Function to hook is defined here
        function showStacks() {
                Java.perform(function () {
                            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
                        });
        };

        function hookURLAndHttp() {
            var URL = Java.use('java.net.URL');
            var HttpURLConnection = Java.use('java.net.HttpURLConnection');
        
            // Hook URL 构造函数
            URL.$init.overload('java.lang.String').implementation = function (url) {
                console.log('加密前URL：' + url);
                showStacks(); // 假设 showStacks 是一个已定义的函数，用于显示堆栈信息
                return this.$init(url);
            };
        
            // Hook openConnection 方法
            URL.openConnection.overload().implementation = function () {
                var connection = this.openConnection();
                console.log('openConnection called: ' + this.toString());
                return connection;
            };
        
            // Hook HttpURLConnection 的 connect 方法
            HttpURLConnection.connect.implementation = function () {
                console.log('HttpURLConnection.connect called');
                return this.connect();
            };
        
            // Hook getOutputStream 方法（拦截请求体）
            HttpURLConnection.getOutputStream.implementation = function () {
                var outputStream = this.getOutputStream();
                var ByteArrayOutputStream = Java.use('java.io.ByteArrayOutputStream');
                var byteArrayOutputStream = ByteArrayOutputStream.$new();
        
                var myOutputStream = Java.use('java.io.OutputStream').extend({
                    write: function(buffer, offset, len) {
                        byteArrayOutputStream.write(buffer, offset, len);
                        outputStream.write(buffer, offset, len);
                    },
                    close: function() {
                        outputStream.close();
                        console.log('Request Body: ' + byteArrayOutputStream.toString());
                    },
                    flush: function() {
                        outputStream.flush();
                    }
                });
        
                return myOutputStream.$new();
            };
        
            // Hook getInputStream 方法（拦截响应体）
            HttpURLConnection.getInputStream.implementation = function () {
                var inputStream = this.getInputStream();
                var BufferedInputStream = Java.use('java.io.BufferedInputStream');
                var ByteArrayOutputStream = Java.use('java.io.ByteArrayOutputStream');
        
                var bufferedInputStream = BufferedInputStream.$new(inputStream);
                var byteArrayOutputStream = ByteArrayOutputStream.$new();
                var buffer = Java.array('byte', [1024]);
                var length;
        
                while ((length = bufferedInputStream.read(buffer)) != -1) {
                    byteArrayOutputStream.write(buffer, 0, length);
                }
        
                console.log('Response Body: ' + byteArrayOutputStream.toString());
                return inputStream;
            };
        };
        
        hookURLAndHttp();

        });

    """

    js = """
        Java.perform(() => {
        // Function to hook is defined here
        function showStacks() {
                Java.perform(function () {
                            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
                        });
        };

        function hookOkHttp() {
            var HttpUrl = Java.use('com.android.okhttp.HttpUrl');
            var HttpReq = Java.use('com.android.okhttp.Request');
            // Hook url 方法
            HttpUrl.url.overload().implementation = function () {
                var result = this.url();
                console.log('Original URL: ' + result.toString());
                showStacks();
                return result;
            };
        
            HttpReq["url"].implementation = function (a) {
                console.log(`[com.android.okhttp.Request.url] param>> a:${a}`);
                var result = this["url"](a);
                showStacks();
                return result;
            };
            // Hook parse 方法
            HttpUrl.parse.overload('java.lang.String').implementation = function (url) {
                console.log('Original URL (parse): ' + url);
                showStacks();
            };
        };
        
        // 调用 hook 函数
        hookOkHttp();

        });

    """

    js = """
        Java.perform(() => {
        // Function to hook is defined here
        function showStacks() {
                Java.perform(function () {
                            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
                        });
        };

        function hook1() {
            var URL = Java.use('java.net.URL');
            URL.$init.overload('java.lang.String').implementation = function (a) {
                console.log('加密前URL：' + a)
                showStacks()
                this.$init(a)
            }
        };
        hook1();

        // hook base
        function hookBase() {
            // Base64
            var Base64Class = Java.use("android.util.Base64");
            Base64Class.encodeToString.overload("[B", "int").implementation = function (a, b) {
                var rc = this.encodeToString(a, b);
                console.log(">>> Base64 " + rc);
                return rc;
            }
        };
        hookBase();

        // hook map
        function hookMap() {
            var Build = Java.use("java.util.HashMap");
            Build["put"].implementation = function (key, val) {
                console.log(`[HashMap算法] -b-`)
                showStacks();
                console.log(`[HashMap] key:【${key}】  val: 【${val}】`)
                console.log(`[HashMap算法] -e-\n\n`)
                return this.put(key, val)
            }
        };
        // hookMap();

        function hook6() {
            var a = Java.use("b1.c");
            a["e"].implementation = function (a, b, c, d, e, f) {
                console.log(`[b1.c.e] param>> a:${a}, b:${b}, c:${c}, d: ${d}, e: ${e}, f：${f}`);
                var result = this["e"](a, b, c, d, e, f);
                console.log("[b1.c.e] result begin");
                console.log(result);
                console.log("[b1.c.e] result end");
                showStacks();
                return result;
            };
        };
        hook6();

        function hook7() {
            var a = Java.use("o5.e");
            a["d"].implementation = function (a, b, c, d) {
                console.log(`[o5.e.d] param>> a:${a}, b:${b}, c:${c}, d: ${d}`);
                var result = this["d"](a, b, c, d);
                console.log("[o5.e.d] result begin");
                console.log(result);
                console.log("[o5.e.d] result end");
                showStacks();
                return result;
            };
        };
        hook7();

        });

    """


    js = """
        Java.perform(() => {
        // Function to hook is defined here
        console.log("[开始] hook")
        function showStacks() {
                Java.perform(function () {
                            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
                        });
        };

        function hook1() {
            var URL = Java.use('java.net.URL');
            URL.$init.overload('java.lang.String').implementation = function (a) {
                console.log('---hook1-begin---')
                console.log('加密前URL：' + a)
                showStacks()
                this.$init(a)  // 执行原函数
                showStacks()
                console.log('---hook1-end---')
            }
        };
        hook1();
        
        function hook6() {
            var a = Java.use("b1.c");
            var g5_b = Java.use("g5.b")
            g5_b["e"].implementation = function (a, b, c, d, e, f) {
                console.log(`[b1.c.e] param>> a:${a}, b:${b}, c:${c}, d: ${d}, e: ${e}, f：${f}`);
                console.log(`[b1.c类属性]: a.B: ${a.B} a.d: ${a.d} a.f: ${a.f} a.g: ${a.g} a.h: ${a.h}  a.i: ${a.i}  `)
                console.log(`[g5.b.i]  this.p: ${g5_b.i()}`)
                var result = this["e"](a, b, c, d, e, f);
                console.log("[b1.c.e] result begin");
                console.log(result);
                console.log("[b1.c.e] result end");
                showStacks();
                return result;
            };
        };
        hook6();
        
       function hook60() {
            var a = Java.use("b1.c");
            a["f"].implementation = function (a, b, c) {
                console.log(`[b1.c.f] param>> a:${a}, b:${b}, c:${c}`);
                console.log(`[b1.c类属性]: a.B: ${a.B} a.d: ${a.d} a.f: ${a.f} a.g: ${a.g} a.h: ${a.h}  a.i: ${a.i}  `)
                var result = this["f"](a, b, c);
                console.log("[b1.c.f] result begin");
                console.log(result);
                console.log("[b1.c.f] result end");
                showStacks();
                return result;
            };
        };
        hook60();
        
        
        function hook601() {
            var a = Java.use("b1.c");
            a["t"].implementation = function (a, b, c) {
                console.log(`[b1.c.t] param>> a:${a}, b:${b}, c:${c}`);
                console.log(`[b1.t类属性]: a.B: ${a.B} a.d: ${a.d} a.f: ${a.f} a.g: ${a.g} a.h: ${a.h}  a.i: ${a.i}  `)
                var result = this["t"](a, b, c);
                console.log("[b1.c.t] result begin");
                console.log(result);
                console.log("[b1.c.t] result end");
                showStacks();
                return result;
            };
        };
        hook601();

       function hook61() {
            var a = Java.use("o5.e");
            a["e"].implementation = function (a, b) {
                console.log(`[o5.e.e] param>> a:${a}, b:${b}`);
                var result = this["e"](a, b);
                console.log("[o5.e.e] result begin");
                console.log(result);
                console.log("[o5.e.e] result end");
                showStacks();
                return result;
            };
        };
        hook61();
        
        function hook62() {
            var a = Java.use("o5.e");
            a["f"].implementation = function (a, b, c) {
                console.log(`[o5.e.f] param>> a:${a}, b:${b}, d:${c}`);
                var result = this["f"](a, b, c);
                console.log("[o5.e.f] result begin");
                console.log(result);
                console.log("[o5.e.f] result end");
                showStacks();
                return result;
            };
        };
        hook62();
        
        function hook7() {
            var a = Java.use("o5.e");
            a["d"].implementation = function (a, b, c, d) {
                console.log(`[o5.e.d] param>> a:${a}, b:${b}, c:${c}, d: ${d}`);
                var result = this["d"](a, b, c, d);
                console.log("[o5.e.d] result begin");
                console.log(result);
                console.log("[o5.e.d] result end");
                showStacks();
                return result;
            };
        };
        hook7();

        });
    console.log("[结束] hook")
    """


    script = session.create_script(js)

    # 设置消息回调函数
    script.on('message', on_message)

    # 加载并运行脚本
    script.load()

    # 保持脚本运行，直到按下 Ctrl+C 或者脚本自行退出
    try:
        sys.stdin.read()
    except KeyboardInterrupt:
        pass

    # 断开连接并清理资源
    session.detach()
    print("[*] Script finished and detached.")


if __name__ == '__main__':
    # target_app = 'com.firstsechk.tc.trade'
    # target_app = '第一证券(香港)'

    process_matches = ['firstsechk', '第一证券']  # 自动匹配所需进程，有时进程名会在两个之间变化
    main(process_matches)
