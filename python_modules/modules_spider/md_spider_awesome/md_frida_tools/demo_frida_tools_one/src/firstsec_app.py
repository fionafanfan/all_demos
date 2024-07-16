#!/usr/bin/env python

import sys
import frida


def hook():

    def on_message(message, data):
        if message["type"] == "send":
            print("[*]{0}".format(message["payload"]))
        else:
            print(message)

    rdev = frida.get_remote_device()
    session = rdev.attach("第一证券(香港)")

 
    src = """
        Java.perform(function(){
            let C0346c = Java.use("b1.c");
            C0346c["j"].implementation = function (str) {
                send(str);
                let result = this["j"](str);
                console.log(`C0346c.mo1806j result=${result}`);
                return result;
            };
            let C0075f = Java.use("android.support.v4.media.f");
            C0075f["q"].implementation = function (bArr) {
                send(bArr);
                let result = this["q"](bArr);
                console.log(`C0075f.m510q result=${result}`);
                return result;
            };
        })
    """

    script = session.create_script(src)
    script.on("message", on_message)
    print("[*] running...")
    script.load()

    sys.stdin.read()


if __name__ == '__main__':
    hook()
