import frida
import sys

"""
[*] Running Class Enumeration
[*] com.afe.mobilecore.tcuicore.RootBaseActivity
[*] com.afe.mobilecore.tcuicore.SplashBaseActivity
[*] Enumeration complete
"""
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function() {
    Java.enumerateLoadedClasses({
        onMatch: function(className) {
            if (className.indexOf('com.afe.mobilecore.tcuicore') !== -1) {
                send(className);
            }
        },
        onComplete: function() {
            send('Enumeration complete');
        }
    });
});
"""

jscode = """
Java.perform(function() {
    Java.enumerateLoadedClasses({
        onMatch: function(className) {
                send(className);
        },
        onComplete: function() {
            send('Enumeration complete');
        }
    });
});
"""

jscode = """
Java.perform(function() {
    Java.enumerateLoadedClasses({
        onMatch: function(className) {
            if (className.indexOf('firstsechk') !== -1) {
                send(className);
            }
        },
        onComplete: function() {
            send('Enumeration complete');
        }
    });
});
"""
process = frida.get_usb_device().attach('com.firstsechk.tc.trade')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running Class Enumeration')
script.load()
sys.stdin.read()
