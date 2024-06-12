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
    Java.perform(function() {
    // Convert byte array to hex string
    function byteArrayToHex(byteArray) {
        return Array.prototype.map.call(byteArray, function(byte) {
            return ('0' + (byte & 0xFF).toString(16)).slice(-2);
        }).join('');
    }
    
    function bytesToHex(byteArray) {
        var HexClass = Java.use('javax.xml.bind.DatatypeConverter');
        return HexClass.printHexBinary(byteArray);
    }
    
    function hook1() {
        var URL = Java.use('java.net.URL');
        URL.$init.overload('java.lang.String').implementation = function (a) {
            console.log('---hook1-begin---')
            console.log('URL：' + a)
            this.$init(a)
            console.log('---hook1-end---')
        }
    };
    hook1();

    function hook7() {
        var a = Java.use("o5.e");
        a["d"].implementation = function (a, b, c, d) {
            console.log(`[o5.e.d] param>> a:${a}, b:${b}, c:${c}, d: ${d}`);
            var result = this["d"](a, b, c, d);
            console.log("[o5.e.d] result begin");
            console.log(result);
            console.log("[o5.e.d] result end");
            return result;
        };
    };
    hook7();
        
    // 获取目标类
    var LoginClass = Java.use('b1.c');

    // Hook目标方法
    LoginClass.e.overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'int', 'java.lang.String').implementation = function(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5) {
        console.log('Hooked LoginClass.e()');

        // 打印传入参数
        console.log('paramString1: ' + paramString1);
        console.log('paramString2: ' + paramString2);
        console.log('paramString3: ' + paramString3);
        console.log('paramString4: ' + paramString4);
        console.log('paramInt: ' + paramInt);
        console.log('paramString5: ' + paramString5);

        // 调用原始方法
        var result = this.e(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5);

        // 打印返回值
        console.log('Result: ' + result);

        return result;
    };

    // hook g5.b.e 获取成功
    var g5_b = Java.use("g5.b")
    g5_b["e"].implementation = function (a, b) {
        console.log(`[g5.b.e] param>> a:${a}, b:${b}`);
        var result = this["e"](a, b);
        console.log("[g5.b.e] result begin");
        console.log(`[g5.b.e] result: ${result}`);
        console.log("[g5.b.e] result end");
        return result;
    };
            
    // Hook KeyGenerator.getInstance
    var KeyGenerator = Java.use('javax.crypto.KeyGenerator');
    KeyGenerator.getInstance.overload('java.lang.String').implementation = function(algorithm) {
        console.log('KeyGenerator.getInstance called with algorithm: ' + algorithm);
        var keyGen = this.getInstance(algorithm);
        return keyGen;
    };

    // Hook KeyFactory.getInstance
    var KeyFactory = Java.use('java.security.KeyFactory');
    KeyFactory.getInstance.overload('java.lang.String').implementation = function(algorithm) {
        console.log('KeyFactory.getInstance called with algorithm: ' + algorithm);
        var keyFactory = this.getInstance(algorithm);
        return keyFactory;
    };
    
    // Hook SecretKeyFactory.getInstance
    var SecretKeyFactory = Java.use('javax.crypto.SecretKeyFactory');
    SecretKeyFactory.getInstance.overload('java.lang.String').implementation = function(algorithm) {
        console.log('SecretKeyFactory.getInstance called with algorithm: ' + algorithm);
        var secretKeyFactory = this.getInstance(algorithm);
        return secretKeyFactory;
    };

    // Hook PBEKeySpec constructor
    var PBEKeySpec = Java.use('javax.crypto.spec.PBEKeySpec');
    PBEKeySpec.$init.overload('[C', '[B', 'int', 'int').implementation = function(password, salt, iterationCount, keyLength) {
        console.log('PBEKeySpec created with password: ' + password + ', salt: ' + byteArrayToHex(salt) + ', iterationCount: ' + iterationCount + ', keyLength: ' + keyLength);
        return this.$init(password, salt, iterationCount, keyLength);
    };

    // Hook Cipher.getInstance
    var Cipher = Java.use('javax.crypto.Cipher');
    Cipher.getInstance.overload('java.lang.String').implementation = function(transformation) {
        console.log('Cipher.getInstance called with transformation: ' + transformation);
        var cipher = this.getInstance(transformation);
        return cipher;
    };

    // Hook Cipher.init
    Cipher.init.overload('int', 'java.security.Key').implementation = function(opmode, key) {
        var keyClass = Java.use('java.security.Key');
        var keySpecClass = Java.use('javax.crypto.spec.SecretKeySpec');
        
        var keyAlgorithm = key.getAlgorithm();  // 获取密钥的算法
        var keyFormat = key.getFormat();  // 获取密钥的格式
        var keyEncoded = key.getEncoded();  // 获取密钥的内容
        
        // 打印关键信息
        console.log('Cipher.init called with opmode: ' + opmode);
        console.log('Key Algorithm: ' + keyAlgorithm);  
        console.log('Key Format: ' + keyFormat); 
        console.log('Key Encoded: ' + keyEncoded);  
        console.log('Key Encoded（16进制编码）: ' + byteArrayToHex(keyEncoded))
        this.init(opmode, key);
    };

    // Hook Cipher.doFinal
    Cipher.doFinal.overload('[B').implementation = function(data) {
        console.log('Cipher.doFinal called with data: ' + data);
        var result = this.doFinal(data);
        console.log('Cipher.doFinal result: ' + result);
        return result;
    };
});

        function hook601() {
            var a = Java.use("b1.c");
            a["t"].implementation = function (a, b, c) {
                console.log(`[b1.c.t] param>> a:${a}, b:${b}, c:${c}`);
                console.log(`[b1.t类属性]: a.B: ${a.B} a.d: ${a.d} a.f: ${a.f} a.g: ${a.g} a.h: ${a.h}  a.i: ${a.i}  `)
                var result = this["t"](a, b, c);
                console.log("[b1.c.t] result begin");
                console.log(result);
                console.log("[b1.c.t] result end");w
                return result;
            };
        };
        hook601();
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
