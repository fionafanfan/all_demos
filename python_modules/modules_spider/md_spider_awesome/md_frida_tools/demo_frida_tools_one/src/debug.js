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
