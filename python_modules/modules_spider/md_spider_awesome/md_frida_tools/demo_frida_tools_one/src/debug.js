// 放置在Java.perform(() => {your_code})中

// 打印堆栈信息
function showStack(className) {
    var Log = Java.use('android.util.Log');
    var Exception = Java.use('java.lang.Exception');
    var stackTrace = Log.getStackTraceString(Exception.$new());
    console.log(`[${className}] 堆栈信息: ` + stackTrace);
}

// 打印堆栈信息， 不传参
function showStacks() {
    Java.perform(function () {
                console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
            });
};

// demo临时调试------------------------------------------------------------------------------------------------------
// var URL = Java.use('java.net.URL');
// URL.$init.overload('java.lang.String').implementation = function (a) {
//     console.log('java.net.URL参数：' + a)
//     showStack()
//     this.$init(a)
// }

// hook所有实现OnClick的类v1------------------------------------------------------------------------------------------------------
// Java.enumerateLoadedClasses({
//     onMatch: function (className) {
//         // 使用 try-catch 以防类加载失败
//         try {
//             // 获取类的引用
//             var clazz = Java.use(className);

//             // 检查类是否实现了 OnClickListener 接口
//             if (Java.use('android.view.View$OnClickListener').class.isInstance(clazz)) {
//                 console.log('Found OnClickListener: ' + className);

//                 // 钩取 onClick 方法
//                 clazz.onClick.implementation = function (view) {
//                     console.log('onClick called in: ' + className + ' with view: ' + view);
                    
//                     // 调用原始的 onClick 方法
//                     this.onClick(view);
//                 };
//             }
//         } catch (e) {
//             // 捕获异常并输出到控制台
//             console.log('Error: ' + e.message);
//         }
//     },
//     onComplete: function () {
//         console.log('Class enumeration complete');
//     }
// });


// hook所有实现OnClick的类v2------------------------------------------------------------------------------------------------------
// var OnClickListener = Java.use('android.view.View$OnClickListener');
// // 获取所有的类
// Java.enumerateLoadedClasses({
//     onMatch: function (className) {
//         try {
//             var clazz = Java.use(className);
            
//             // 获取类实现的接口
//             var interfaces = clazz.class.getInterfaces();
            
//             // 检查类是否实现了 OnClickListener 接口
//             for (var i = 0; i < interfaces.length; i++) {
//                 if (interfaces[i].getName() === 'android.view.View$OnClickListener') {
//                     console.log('Found OnClickListener: ' + className);

//                     // 钩取 onClick 方法
//                     clazz.onClick.implementation = function (view) {
//                         console.log(`[${className}] onClick called in: ` + ' with view: ' + view);
//                         // 显示堆栈信息
//                         showStack(className);
//                         // 调用原始的 onClick 方法
//                         this.onClick(view);
//                     };
//                     break;
//                 }
//             }
//         } catch (e) {
//             // 捕获异常并输出到控制台
//             if (e.message.indexOf('java.lang.ClassNotFoundException') != -1) {
//                 console.log('ClassNotFound: ' + className);
//             } else {
//                 console.log('Other Error: ' + e.message);
//             }
//         }
//     },
//     onComplete: function () {
//         console.log('Class enumeration complete');
//     }
// });

// hook所有实现OnCreate的类-失败，有些onCreate------------------------------------------------------------------------------------------------------
// Java.enumerateLoadedClasses({
//     onMatch: function (className) {
//         try {
//             var classInstance  = Java.use(className);
//             if (classInstance.onCreate) {
//                 classInstance.onCreate.overload('android.os.Bundle').implementation = function (param) {
//                     console.log(`[${className}] onCreate called in: ` + ' with param: ' + param);
//                     this.onCreate.apply(this, arguments);
//                 };
//             }
//         } catch (e) {
//             // 捕获异常并输出到控制台
//             if (e.message.indexOf('java.lang.ClassNotFoundException') != -1) {
//                 console.log('ClassNotFound: ' + className);
//             } else {
//                 console.log('Other Error: ' + e.message);
//             }
//         }
//     },
//     onComplete: function () {
//         console.log('Class enumeration complete');
//     }
// });

// hook实现k1.c.OnCreate的类------------------------------------------------------------------------------------------------------
// function hook6() {
//     var obj = Java.use("k1.c");
//     obj.onCreate.implementation = function (a) {
//         console.log(`[k1.c.onCreate] param>> a:${a}`);
//         var result = this["onCreate"](a);
//         console.log("[k1.c.onCreate] result begin");
//         console.log(`[k1.c.onCreate] result: ${result}`);
//         console.log("[k1.c.onCreate] result end");
//         showStacks()
//         return result
//     };
// };
// hook6();


// hook实现k1.c.setTitle的类------------------------------------------------------------------------------------------------------
// function hook() {
//     var obj = Java.use("k1.c");
//     obj.setTitle.implementation = function (a) {
//         console.log(`[k1.c.setTitle] param>> a:${a}`);
//         var result = this["setTitle"](a);
//         console.log("[k1.c.setTitle] result begin");
//         console.log(`[k1.c.setTitle] result: ${result}`);
//         console.log("[k1.c.setTitle] result end");
//         showStacks()
//         return result
//     };
// };
// hook();


// hook实现k1.c.setText------------------------------------------------------------------------------------------------------
function hook() {
    var obj = Java.use("android.widget.TextView");

    obj['setText'].overloads.forEach(function (overload) {
    overload.implementation = function (a) {
            console.log('[+] ' + overload + ' - ' + 'setText' + ' called: ' + 'param: ' + a);
            console.log('Arguments: ' + JSON.stringify(arguments));
            var res = overload.apply(this, arguments);
            showStack();
            return res
        };
    });
};
hook();

// hook网络请求------------------------------------------------------------------------------------------------------
// 钩取 HttpURLConnection 的网络请求方法
// var HttpURLConnection = Java.use('java.net.HttpURLConnection');
// HttpURLConnection.getInputStream.implementation = function () {
//     console.log('[+] HttpURLConnection - getInputStream called');
//     console.log('URL: ' + this.getURL().toString());
//     return this.getInputStream();
// };

// HttpURLConnection.getOutputStream.implementation = function () {
//     console.log('[+] HttpURLConnection - getOutputStream called');
//     console.log('URL: ' + this.getURL().toString());
//     return this.getOutputStream();
// };

// // 钩取 OkHttp 的网络请求方法
// var OkHttpClient = Java.use('com.android.okhttp.OkHttpClient');
// var Request = Java.use('com.android.okhttp.Request');
// var Call = Java.use('com.android.okhttp.Call');
// var Response = Java.use('com.android.okhttp.Response');

// OkHttpClient.newCall.overload('com.android.okhttp.Request').implementation = function (request) {
//     console.log('[+] OkHttpClient - newCall called');
//     console.log('URL: ' + request.url().toString());
//     return this.newCall(request);
// };

// // 通用的网络请求钩取方法
// function hookAllMethods(className, methodName) {
//     var clazz = Java.use(className);
//     clazz[methodName].overloads.forEach(function (overload) {
//         overload.implementation = function () {
//             console.log('[+] ' + className + ' - ' + methodName + ' called');
//             console.log('Arguments: ' + JSON.stringify(arguments));
//             var res = overload.apply(this, arguments);
//             showStack();
//             return res
//         };
//     });
// }

// // 示例：钩取所有 com.android.okhttp 包内的类和方法
// hookAllMethods('com.android.okhttp.Request$Builder', 'build');
// hookAllMethods('com.android.okhttp.Call', 'enqueue');
// hookAllMethods('com.android.okhttp.Call', 'execute');

// // 钩取 Apache HttpClient 的网络请求方法
// var DefaultHttpClient = Java.use('org.apache.http.impl.client.DefaultHttpClient');
// var HttpRequestBase = Java.use('org.apache.http.client.methods.HttpRequestBase');

// DefaultHttpClient.execute.overload('org.apache.http.client.methods.HttpUriRequest').implementation = function (request) {
//     console.log('[+] DefaultHttpClient - execute called');
//     console.log('URL: ' + request.getURI().toString());
//     return this.execute(request);
// };

// DefaultHttpClient.execute.overload('org.apache.http.client.methods.HttpUriRequest', 'org.apache.http.protocol.HttpContext').implementation = function (request, context) {
//     console.log('[+] DefaultHttpClient - execute with context called');
//     console.log('URL: ' + request.getURI().toString());
//     return this.execute(request, context);
// };

// // 通用的网络请求钩取方法
// function hookAllMethods(className, methodName) {
//     var clazz = Java.use(className);
//     clazz[methodName].overloads.forEach(function (overload) {
//         overload.implementation = function () {
//             console.log('[+] ' + className + ' - ' + methodName + ' called');
//             console.log('Arguments: ' + JSON.stringify(arguments));
//             return overload.apply(this, arguments);
//         };
//     });
// }

// // 示例：钩取 Retrofit 网络请求方法
// hookAllMethods('retrofit2.Retrofit', 'create');
// hookAllMethods('retrofit2.Call', 'enqueue');
// hookAllMethods('retrofit2.Call', 'execute');

// console.log('Network request hooks set up');

// // hook java.net
// var HttpURLConnection = Java.use('java.net.HttpURLConnection');

// // 钩取 setRequestProperty 方法
// HttpURLConnection.setRequestProperty.overload('java.lang.String', 'java.lang.String').implementation = function (key, value) {
//     console.log('[+] HttpURLConnection - setRequestProperty called');
//     console.log('Header: ' + key + ' = ' + value);
//     return this.setRequestProperty(key, value);
// };

// // 钩取 addRequestProperty 方法
// HttpURLConnection.addRequestProperty.overload('java.lang.String', 'java.lang.String').implementation = function (key, value) {
//     console.log('[+] HttpURLConnection - addRequestProperty called');
//     console.log('Header: ' + key + ' = ' + value);
//     return this.addRequestProperty(key, value);
// };

// // 钩取 getInputStream 方法
// HttpURLConnection.getInputStream.implementation = function () {
//     console.log('[+] HttpURLConnection - getInputStream called');
//     var headers = this.getRequestProperties();
//     var headerKeys = headers.keySet().toArray();
//     for (var i = 0; i < headerKeys.length; i++) {
//         var key = headerKeys[i];
//         var values = headers.get(key).toArray();
//         for (var j = 0; j < values.length; j++) {
//             console.log('Header: ' + key + ' = ' + values[j]);
//         }
//     }
//     return this.getInputStream();
// };

// // 钩取 getOutputStream 方法
// HttpURLConnection.getOutputStream.implementation = function () {
//     console.log('[+] HttpURLConnection - getOutputStream called');
//     var headers = this.getRequestProperties();
//     var headerKeys = headers.keySet().toArray();
//     for (var i = 0; i < headerKeys.length; i++) {
//         var key = headerKeys[i];
//         var values = headers.get(key).toArray();
//         for (var j = 0; j < values.length; j++) {
//             console.log('Header: ' + key + ' = ' + values[j]);
//         }
//     }
//     return this.getOutputStream();
// };

// console.log('HTTP request hooks set up');

