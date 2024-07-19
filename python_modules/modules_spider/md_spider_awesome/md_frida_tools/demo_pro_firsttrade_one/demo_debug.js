//  ¡¾b¡¿¡¾hook1¡¿
Java.perform(function() {
    var URL = Java.use("java.net.URL");
    var HttpURLConnection = Java.use("java.net.HttpURLConnection");

    URL.openConnection.overload().implementation = function() {
        var connection = this.openConnection();

        if (connection.getClass().getName() === 'com.android.okhttp.internal.huc.HttpURLConnectionImpl' ||
            connection.getClass().getName() === 'com.android.okhttp.internal.huc.DelegatingHttpsURLConnection' ||
            connection.getClass().getName() === 'com.android.okhttp.internal.huc.HttpsURLConnectionImpl') {

            // Hook connect method to intercept request headers
            connection.connect.implementation = function() {
                send("URL: " + this.getURL().toString());

                // Get and log request headers
                var headers = this.getRequestProperties();
                var headerString = "Request Headers: ";
                headers.entrySet().forEach(function(entry) {
                    headerString += entry.getKey() + ": " + entry.getValue() + ", ";
                });
                send(headerString);

                this.connect();
            };

            // Hook getOutputStream to intercept request body
            connection.getOutputStream.implementation = function() {
                var outputStream = this.getOutputStream();
                send("Request body intercepted");
                return outputStream;
            };

            // Hook getInputStream to intercept response body
            connection.getInputStream.implementation = function() {
                var inputStream = this.getInputStream();
                send("Response code: " + this.getResponseCode());

                // Get and log response headers
                var responseHeaders = this.getHeaderFields();
                var responseHeaderString = "Response Headers: ";
                responseHeaders.entrySet().forEach(function(entry) {
                    responseHeaderString += entry.getKey() + ": " + entry.getValue() + ", ";
                });
                send(responseHeaderString);

                send("Response body intercepted");
                return inputStream;
            };
        }

        return connection;
    };
});
//  ¡¾e¡¿¡¾hook1¡¿


//  ¡¾b¡¿¡¾hook2¡¿
Java.perform(function() {
    var URL = Java.use("java.net.URL");
    var HttpURLConnection = Java.use("java.net.HttpURLConnection");

    URL.openConnection.overload().implementation = function() {
        var connection = this.openConnection();

        if (connection.getClass().getName() === 'com.android.okhttp.internal.huc.HttpURLConnectionImpl' ||
            connection.getClass().getName() === 'com.android.okhttp.internal.huc.DelegatingHttpsURLConnection' ||
            connection.getClass().getName() === 'com.android.okhttp.internal.huc.HttpsURLConnectionImpl') {

            // Hook connect method to intercept request headers
            connection.connect.implementation = function() {
                send("URL: " + this.getURL().toString());

                // Get and log request headers
                var headers = this.getRequestProperties();
                var headerString = "Request Headers: ";
                headers.entrySet().forEach(function(entry) {
                    headerString += entry.getKey() + ": " + entry.getValue() + ", ";
                });
                send(headerString);

                this.connect();
            };

            // Hook getOutputStream to intercept request body
            connection.getOutputStream.implementation = function() {
                var outputStream = this.getOutputStream();
                send("Request body intercepted");
                return outputStream;
            };

            // Hook getInputStream to intercept response body
            connection.getInputStream.implementation = function() {
                var inputStream = this.getInputStream();
                send("Response code: " + this.getResponseCode());

                // Get and log response headers
                var responseHeaders = this.getHeaderFields();
                var responseHeaderString = "Response Headers: ";
                responseHeaders.entrySet().forEach(function(entry) {
                    responseHeaderString += entry.getKey() + ": " + entry.getValue() + ", ";
                });
                send(responseHeaderString);

                send("Response body intercepted");
                return inputStream;
            };
        }

        return connection;
    };
});
//  ¡¾e¡¿¡¾hook2¡¿