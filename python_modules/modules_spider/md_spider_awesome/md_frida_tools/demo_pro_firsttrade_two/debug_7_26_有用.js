    Java.perform(function() {
    // ============== 定义公共方法 begin================
    // ===============================================

    // 将字节数组转为十六进制字符串
    function byteArrayToHex(byteArray) {
        return Array.prototype.map.call(byteArray, function(byte) {
            return ('0' + (byte & 0xFF).toString(16)).slice(-2);
        }).join('');
    }

    // 打印堆栈信息
    function showStacks() {
        Java.perform(function () {
                    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
                });
    };
    // ===============================================
    // ============== 定义公共方法 end===================


    // ============== 定义hook方法 begin================
    // ===============================================
    function hook_java_net_URL() {
        var URL = Java.use('java.net.URL');
        URL.$init.overload('java.lang.String').implementation = function (the_url) {
            console.log('[java.net.URL] URL---：' + the_url)
            this.$init(the_url)
        }

    };

    function hook_java_net_URL_track() {
        var URL = Java.use('java.net.URL');
        URL.$init.overload('java.lang.String').implementation = function (url) {
            console.log('[java.net.URL track] [track] URL：' + url);
            showStacks();
            this.$init(url);
        }

    };


    function hook_o5_e_d() {
        var o5_e = Java.use("o5.e");
        o5_e["d"].implementation = function (a, b, c, d) {
            console.log(`[o5.e.d] param>> a:${a}, b:${b}, c:${c}, d: ${d}`);
            var result = this["d"](a, b, c, d);
            console.log("[o5.e.d] result begin");
            console.log(`[o5.e.d]result: ${result}`);
            console.log("[o5.e.d] result end");

            return result;
        };
    };


    function hook_b1_c_t() {
        var b1_c = Java.use("b1.c");
        b1_c["t"].implementation = function (a, b, c) {
            console.log(`[b1.c.t] param>> a:${a}, b:${b}, c:${c}`);
            console.log(`[b1.t类属性]: a.B: ${a.B} a.d: ${a.d} a.f: ${a.f} a.g: ${a.g} a.h: ${a.h}  a.i: ${a.i}  `)
            var result = this["t"](a, b, c);
            console.log("[b1.c.t] result begin");
            console.log(`[b1.c.t] result: ${result}`);
            console.log("[b1.c.t] result end");
            return result;
        };
    };


    function hook_b1_c_e() {
        // 获取目标类
        var b1_c = Java.use('b1.c');

        // Hook目标方法
        b1_c.e.overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'int', 'java.lang.String').implementation = function(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5) {
            // 打印传入参数
            console.log('[b1.c.e]paramString1: ' + paramString1);
            console.log('[b1.c.e]paramString2: ' + paramString2);
            console.log('[b1.c.e]paramString3: ' + paramString3) ;
            console.log('[b1.c.e]paramString4: '  + paramString4);
            console.log('[b1.c.e]paramInt: ' + paramInt);
            console.log('[b1.c.e]paramString5: ' + paramString5);

            // 调用原始方法
            var result = this.e(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5);

            // 打印返回值
            console.log('[b1.c.e]Result: ' + result);
            return result;
        };

    };
    // === 新加hook， 待验证hook begin===

    function hook_b1_c_a() {
        // 获取目标类
        var b1_c = Java.use('b1.c');

        // Hook目标方法
        b1_c.a.overload('long', 'int', 'java.lang.String').implementation = function(p1, p2, p3) {
            // 打印传入参数
            console.log(`[b1.c.a] param>> p1:${p1}, p2:${p2},  p3:${p3}, `);

            // 调用原始方法
            var result = this.a(p1, p2, p3);

            // 打印返回值
            console.log('[b1.c.a]Result: ' + result);
            return result;
        };

    };

    function hook_b1_c_q() {
      var b1_c = Java.use('b1.c');
      b1_c["q"].implementation = function (p1, p2, p3) {
            console.log(`[b1.c.q] p1=${p1};  p2=${p2};  p3=${p3}`);
            let result = this["q"](p1, p2, p3);
            console.log(`[b1.c.q] result=${result}`);
            return result;
        };

    };

    function hook_g5_b_f() {
      var g5_b = Java.use('g5.b');
      g5_b["F"].implementation = function (p1, p2, p3) {
            console.log(`[g5.b.F] p1=${p1};  p2=${p2};  p3=${p3}`);
            let result = this["F"](p1, p2, p3);
            console.log(`[g5.b.F] result=${result}`);
            return result;
        };

    };

    function  hook_b1_c_j() {
      let b1_c = Java.use("b1.c");
      b1_c["j"].implementation = function (str) {
            console.log(`[b1.c.j] param=${str}`);
            send(str);
            let result = this["j"](str);
            console.log(`[b1.c.j] result=${result}`);
            return result;
        };
    };

    function  hook_o5_c_run() {
      var o5_c = Java.use('o5.c');
      o5_c["run"].implementation = function () {
            console.log(`[o5.c.run]`);
            let result = this["run"]();
            console.log(`[o5.c.run] result=${result}`);
            return result;
        };
    };

    function  hook_o5_e_c() {
      var o5_d = Java.use('o5.e');
      o5_d["c"].implementation = function (p1) {
            console.log(`[o5.e.c] p1:${p1}`);
            let result = this["c"](p1);
            console.log(`[o5.e.c] result=${result}`);
            return result;
        };
    };

    function hook_android_support_v4_media(){
        // android.support.v4.media.f.z
           let obj = Java.use("android.support.v4.media.f");
            obj["q"].implementation = function (bArr) {
                console.log(`[android.support.v4.media.f.q] param=${bArr}`);
                send(bArr);
                let result = this["q"](bArr);
                console.log(`[android.support.v4.media.f.q] result=${result}`);
                return result;
            };

            let obj2 = Java.use("android.support.v4.media.g");
            obj2["r0"].implementation = function (a, b, c, d) {
                console.log(`[android.support.v4.media.g.r0] a=${a};  b=${b};  c=${c};  d=${d}`);
                let result = this["q"](a, b, c, d);
                console.log(`[android.support.v4.media.g.r0] result=${result}`);
                return result;
            };

            let obj3 = Java.use("android.support.v4.media.f");
            obj3["z"].implementation = function (a, b, c, d='') {
                console.log(`[android.support.v4.media.f.z] a=${a};  b=${b};  c=${c};  d=${d}`);
                showStacks();
                let result = this["z"](a, b, c, d);
                console.log(`[android.support.v4.media.f.z] result=${result}`);

                return result;
            };

            let obj4 = Java.use("android.support.v4.media.f");
            obj4["z"].implementation = function (a, b, c) {
                console.log(`[android.support.v4.media.f.z-abc] a=${a};  b=${b};  c=${c}`);
                showStacks();
                let result = this["z"](a, b, c);
                console.log(`[android.support.v4.media.f.z-abc] result=${result}`);

                return result;
            };
    }

    // === 新加hook， 待验证hook 结束===
    function hook_g5_b_e() {
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
    };


    function hook_javax_cerpto_KeyGenerator() {
        // Hook KeyGenerator.getInstance
        var KeyGenerator = Java.use('javax.crypto.KeyGenerator');
        KeyGenerator.getInstance.overload('java.lang.String').implementation = function(algorithm) {
            console.log('KeyGenerator.getInstance called with algorithm: ' + algorithm);
            var keyGen = this.getInstance(algorithm);
            return keyGen;
        };
    };


    function hook_java_security_KeyFactory() {
        // Hook KeyFactory.getInstance
        var KeyFactory = Java.use('java.security.KeyFactory');
        KeyFactory.getInstance.overload('java.lang.String').implementation = function(algorithm) {
            console.log('KeyFactory.getInstance called with algorithm: ' + algorithm);
            var keyFactory = this.getInstance(algorithm);
            return keyFactory;
        };
    };


    function hook_javax_crypto_SecretKeyFactory() {
        // Hook SecretKeyFactory.getInstance
        var SecretKeyFactory = Java.use('javax.crypto.SecretKeyFactory');
        SecretKeyFactory.getInstance.overload('java.lang.String').implementation = function(algorithm) {
            console.log('SecretKeyFactory.getInstance called with algorithm: ' + algorithm);
            var secretKeyFactory = this.getInstance(algorithm);
            return secretKeyFactory;
        };
    };


    function hook_javax_crypto_spec_PBEKeySpec() {
        // Hook PBEKeySpec constructor
        var PBEKeySpec = Java.use('javax.crypto.spec.PBEKeySpec');
        PBEKeySpec.$init.overload('[C', '[B', 'int', 'int').implementation = function(password, salt, iterationCount, keyLength) {
            console.log('PBEKeySpec created with password: ' + password + ', salt: ' + byteArrayToHex(salt) + ', iterationCount: ' + iterationCount + ', keyLength: ' + keyLength);
            return this.$init(password, salt, iterationCount, keyLength);
        };
    };


    function hook_java_crypto_Cipher() {
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
    };

    // ===============================================
    // ============== 定义hook方法 end===================


    // ============== 调用hook方法 begin================
    // ===============================================
    hook_java_net_URL();
    // hook_java_net_URL_track();
    hook_o5_e_d();
    hook_b1_c_t();
    hook_b1_c_e();
    hook_b1_c_a();
    hook_b1_c_j();
    hook_g5_b_e();
    hook_javax_cerpto_KeyGenerator();
    hook_java_security_KeyFactory();
    hook_javax_crypto_SecretKeyFactory();
    hook_javax_crypto_spec_PBEKeySpec();
    hook_java_crypto_Cipher();

    // 待认证hook()
    hook_o5_c_run();
    hook_o5_e_c();
    hook_android_support_v4_media();
    hook_b1_c_q();
    hook_g5_b_f();
    // ===============================================
    // ============== 调用hook方法 end==================
});