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
        var keyEncoded = key.getEncoded();  // 获取密钥的格式

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
                console.log("[b1.c.t] result end");
                return result;
            };
        };
        hook601();