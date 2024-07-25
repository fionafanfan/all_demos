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