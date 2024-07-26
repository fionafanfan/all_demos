#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/30 15:57
# @File     : gen_login_data_python_demo.py
# @Desc     :

import hashlib


def h():
    pass


def q5_b_i():
    pass


def g5_b_I(a):
    pass


def i_f(des3_key):
    pass


def e(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5):
    bool2 = not paramString1 or not paramString2
    bool1 = True  # 最后的函数返回值， 如果成功完成参数的加密则返回True， 否则为False
    print(f'bool1: {bool1}  bool2:{bool2}')
    if not bool2:
        print("sendLogin")
        this_init = object()
        this_B = 30
        this_s = ''
        this_t = ''
        this_z = ''

        # 这个应该是没有执行得。
        if not this_s or not this_t or this_z != 1:
            h()

        this_x = paramInt
        this_k = 'xx' # 如果不为None， 则置为None
        if this_k is not None:
            this_k = None

        this_k_o5_e = 'o5_e对象'
        o5_e_a = this_init
        this_q = paramString1
        this_r = paramString1
        this_p = q5_b_i()

        try:
            # des3_key = DES3.adjust_key_parity(hashlib.md5().digest())
            # des3_cipher = DES3.new(des3_key, DES3.MODE_ECB)
            des3_key = ''
            des3_cipher = ''
            paramString1 = ''
        except Exception as e:
            paramString1 = None
            print(e)
            return False

        this_v = paramString1
        lid = ''
        lang = ''
        country = ''
        channel = ''
        remarks = [
            "channel={}".format(channel),
            "country={}".format(country),
            "lang={}".format(lang),
            "lid={}".format(lid),
            "pwd={}".format(paramString2)
        ]

        if paramString4:
            remarks.append("fsec={}".format(g5_b_I(paramString4)))

        if paramString3:
            remarks.append("otp={}".format(paramString3))
            this_m = 3
            if this_m == 3:
                remarks.append("keep_otp_flg={}".format(paramString5))
    p = ''
    remarks.append("key={}".format(i_f(des3_key)))
    remarks.append("ip={}".format(p))

    this_d = ''
    this_e = ''
    this_f = ''
    this_g = ''
    app_info = "{}_{}".format(
        "AppXXX" if not this_d else this_d,
        "x.x.x(x)" if not this_e else this_e
    )

    app_version_info = "x.x" if not this_f else this_f
    brand_info = "UnknownBrand" if not this_g else this_g
    size_info = ''
    remarks.append("remark={}_A{}|{}|{}".format(app_info, app_version_info, size_info, brand_info))
    return bool1



"""
URL: http://trade.firstsechk.com/i-trade/streaming/streamLogin
param: 
re=1&clm=P678%2FfO7GPWmD%2FwpeYdAePFQNoMhC031pTbUsuXSEGpbPZSYvNhvYEdVY2VfDP0quPOH%2BbXZr2Kp%0AuMXd6s38xyrasInrP2EQaoOyp7LRoJRNbpBNg4AoMzQQ70Hfv1YAMkrqOqx4KOOQp0tcienXQf7s%0AcgB26zKfry5wqOWVW5tjGtstaNlIMfejJUGfpo%2FBlqXzLDIYMFT%2BhWCdZZ7L%2FsQA7QySw%2BOzAtgm%0AwfsQE5nRS8QDkiZPYc4eWDz1Rp2909Rtrcg%2B243ZPrj9mIQS%2FKCayyF6E4Oko%2FlBNfmQSai7sQva%0A4FJMFbj3OnYyEYrYyEJhffgQPbSWs2GsMMfsi0lrTB%2FqyM%2F97o8DznRKRp4W1664wAoeuotkqKvE%0Alj3FWv%2F2mdnLrliLBk343rsrn%2F%2BNkU2Sett0gAWV8r0Fpu9E88l8RU7PX7AR3Dg5%2B5%2BBBvDOmB%2FA%0ARTKxbinjVuLGMwYa5v1%2BJNBj91pPjoYStxwGs%2B3E%2BcIhm4fWYMdRQC8xo62DT0F1wkXjm2zgasZy%0AlMWrIb3iUCOhfq0H81dqQQLWP%2FkAbQpOVY%2FGhfhGIfrBImY76JET6TwbkKr9Dw18sVdWCz8KKNJe%0AmcXj%2F%2BXfdSGAJDmvq%2BZKRe8p6S4XQw4kBvXUOG3zu6%2FRgnfPektpVxfpFRsPzO2AH3dUIQv9jVs%3D%0A

re固定为1
clm: remark=为下面的明参经过DESede和RSA等加密 最后转成Base64。 


参数：
remarks必填参数:
channel
country
lang
lid： 账号
pwd: 密码

key 
ip: ip地址
remark: remark 为一些设备信息拼接而成， 拼接的逻辑为：
"{}_A{}|{}|{}".format(app_info, app_version_info, size_info, brand_info)

remarks选填参数：
fsec: 目前观察：如果之前有输入otp， 后面再登录，请求多次，这个参数好像是固定的。
otp： 验证码
keep_otp_flg: 目前观察固定是: F
"""
# [b1.c.e] param>> a:771589S, b:Gr89LM, c:null, d: NmZmMzk2NjktM2VlYy00NjZi, e: 33, f：F
paramString1 = '771589S'  # 代表账号: lid字段
paramString2 = 'Gr89LM'  # 代表密码: pwd字段
paramString3 = None  # 代表验证码: otp字段  , 非初次登录的时候，不用输入otp， 不用输入otp的时候为None
paramString4 = 'NmZmMzk2NjktM2VlYy00NjZi'  # 代表：fsec   目前观察：如果之前有输入otp， 后面再登录，请求多次，这个参数好像是固定的。
paramInt = 33   # 这个参数一直在随机增加
paramString5 = 'F'  # 代表:keep_otp_flg  # 目前观察固定是: F
rt = e(paramString1, paramString2, paramString3, paramString4, paramInt, paramString5)
print(f'rt:{rt}')
