#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/30 15:57
# @File     : gen_login_data_python_demo.py
# @Desc     :

import hashlib
import base64
from Crypto.Cipher import DES3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def e(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5):
    bool2 = not paramString1 or not paramString2
    bool1 = True

    if not bool2:
        print("sendLogin")

        B = 30
        if not self.s or not self.t or self.z != 1:
            h()

        x = paramInt
        if self.k is not None:
            self.k = None

        k = o5.e(B, True)
        self.k = k
        k.a = self

        q = paramString1
        r = paramString1
        p = g5.b.i()

        try:
            des3_key = DES3.adjust_key_parity(hashlib.md5().digest())
            des3_cipher = DES3.new(des3_key, DES3.MODE_ECB)
        except Exception as e:
            print(e)
            return False

        remarks = [
            "channel={}".format(k(self.n)),
            "country={}".format(l(self.m)),
            "lang={}".format(m(self.o)),
            "lid={}".format(q),
            "pwd={}".format(paramString2)
        ]

        if paramString4:
            remarks.append("fsec={}".format(g5.b.I(paramString4)))

        if paramString3:
            remarks.append("otp={}".format(paramString3))
            if self.m == 3:
                remarks.append("keep_otp_flg={}".format(paramString5))

        remarks.append("key={}".format(i.f(des3_key)))
        remarks.append("ip={}".format(p))

        app_info = "{}_{}".format(
            "AppXXX" if not self.d else self.d,
            "x.x.x(x)" if not self.e else self.e
        )

        app_version_info = "x.x" if not self.f else self.f
        brand_info = "UnknownBrand" if not self.g else self.g

        if self.h != -2147483648 and self.i != -2147483648 and not math.isnan(self.j) and self.j > 0.0:
            size_info = "{}x{}_{}in".format(self.h, self.i, round(self.j, 1))
        else:
            size_info = "UnknownSize"

        remarks.append("remark={}_A{}|{}|{}".format(app_info, app_version_info, size_info, brand_info))

        paramString2 = "&".join(remarks)

        try:
            rsa_public_key = RSA.import_key(self.u)
        except Exception as e:
            print(e)
            return False

        if paramString2 and rsa_public_key:
            paramString2 = g5.b.u(paramString2)
            try:
                cipher_rsa = PKCS1_v1_5.new(rsa_public_key)
                enc_data = cipher_rsa.encrypt(paramString2)
            except Exception as e:
                print(e)
                return False

        if not paramString2:
            return False

        encoded_enc_data = g5.b.I(base64.b64encode(enc_data))
        paramString2 = "re=1&clm={}".format(encoded_enc_data)

        print("LoginG2 - {} [{}]".format(self.J, paramString2))

        if not encoded_enc_data:
            print("SecKeyRef AddPublicKey Fail")
        else:
            l1 = self.k.d(1, 0, self.J, paramString2)
            if l1 != -9223372036854775808:
                d(l1, x, 2, f1.d.n)
                self.z = 3
                return True
            else:
                print("SecKeyRef AddPublicKey Fail")

    return bool1
