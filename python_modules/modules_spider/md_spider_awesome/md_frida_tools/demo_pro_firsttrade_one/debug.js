// var OkHttpClient = Java.use('okhttp3.OkHttpClient');
// OkHttpClient.newCall.overload('okhttp3.Request').implementation = function(request) {
//     console.log('OkHttp Request: ' + request.toString());
//     var response = this.newCall(request);
//     return response;
// };


// // hook  okhttp3
// function hookOkhttp3() {
//     var Builder = Java.use('okhttp3.Request$Builder');
//     Builder.url.overload('okhttp3.HttpUrl').implementation = function (a) {
//         console.log('a: ' + a)
//         var res = this.url(a);
//         showStacks()
//         console.log("res: " + res)
//         return res;
//     }
// };


// Java.perform(() => {
// // Function to hook is defined here
// function showStacks() {
//         Java.perform(function () {
//                     console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
//                 });
// };
//
// function hook1() {
//     var URL = Java.use('java.net.URL');
//     URL.$init.overload('java.lang.String').implementation = function (a) {
//         console.log('加密前URL：' + a)
//         showStacks()
//         this.$init(a)
//     }
// };
// hook1();
//
// // hook base
// function hookBase() {
//     // Base64
//     var Base64Class = Java.use("android.util.Base64");
//     Base64Class.encodeToString.overload("[B", "int").implementation = function (a, b) {
//         var rc = this.encodeToString(a, b);
//         console.log(">>> Base64 " + rc);
//         return rc;
//     }
// };
// hookBase();
//
// // hook map
// function hookMap() {
//     var Build = Java.use("java.util.HashMap");
//     Build["put"].implementation = function (key, val) {
//         console.log("[map] key : " + key)
//         console.log("[map] val : " + val)
//         return this.put(key, val)
//     }
// };
// hookMap();
//
// function hook6() {
//     var a = Java.use("b1.c");
//     a["e"].implementation = function (a, b, c, d, e, f) {
//         console.log(`[b1.c.e] param>> a:${a}, b:${b}, c:${c}, d: ${d}, e: ${e}, f：${f}`);
//         var result = this["e"](a, b, c, d, e, f);
//         console.log("[b1.c.e] result begin");
//         console.log(result);
//         console.log("[b1.c.e] result end");
//         showStacks();
//         return result;
//     };
// };
// hook6();
//
// function hook7() {
//     var a = Java.use("o5.e");
//     a["d"].implementation = function (a, b, c, d) {
//         console.log(`[o5.e.d] param>> a:${a}, b:${b}, c:${c}, d: ${d}`);
//         var result = this["d"](a, b, c, d);
//         console.log("[o5.e.d] result begin");
//         console.log(result);
//         console.log("[o5.e.d] result end");
//         showStacks();
//         return result;
//     };
// };
// hook7();
//
// });




// function hook1(){
//     var URL = Java.use('java.net.URL');
//     URL.$init.overload('java.lang.String').implementation= function(a){
//             console.log('加密前：'+a)
//             console.log('                    ')
//             this.$init(a)
//     }
// }
//
// function main(){
//     Java.perform(function(){
//         hook();
//     })
// }
//
//
// setImmediate(main);
