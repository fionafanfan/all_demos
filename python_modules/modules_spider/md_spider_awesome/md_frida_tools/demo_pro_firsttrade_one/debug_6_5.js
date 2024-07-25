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
            console.log('URL��' + a)
            this.$init(a)
            showStacks()
            console.log('---hook1-end---')
        }
    };
    hook1();

    // ��ȡĿ����
    var LoginClass = Java.use('b1.c');

    // HookĿ�귽��
    LoginClass.e.overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'int', 'java.lang.String').implementation = function(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5) {
        console.log('Hooked LoginClass.e()');

        // ��ӡ�������
        console.log('paramString1: ' + paramString1);
        console.log('paramString2: ' + paramString2);
        console.log('paramString3: ' + paramString3);
        console.log('paramString4: ' + paramString4);
        console.log('paramInt: ' + paramInt);
        console.log('paramString5: ' + paramString5);

        // ����ԭʼ����
        var result = this.e(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5);

        // ��ӡ����ֵ
        console.log('Result: ' + result);

        return result;
    };

    // hook g5.b.e ��ȡ�ɹ�
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

        var keyAlgorithm = key.getAlgorithm();  // ��ȡ��Կ���㷨
        var keyFormat = key.getFormat();  // ��ȡ��Կ�ĸ�ʽ
        var keyEncoded = key.getEncoded();  // ��ȡ��Կ������

        // ��ӡ�ؼ���Ϣ
        console.log('Cipher.init called with opmode: ' + opmode);
        console.log('Key Algorithm: ' + keyAlgorithm);
        console.log('Key Format: ' + keyFormat);
        console.log('Key Encoded: ' + keyEncoded);
        console.log('Key Encoded��16���Ʊ��룩: ' + byteArrayToHex(keyEncoded))
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
                console.log(`[b1.t������]: a.B: ${a.B} a.d: ${a.d} a.f: ${a.f} a.g: ${a.g} a.h: ${a.h}  a.i: ${a.i}  `)
                var result = this["t"](a, b, c);
                console.log("[b1.c.t] result begin");
                console.log(result);
                console.log("[b1.c.t] result end");w
                return result;
            };
        };
        hook601();