#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/3 16:00
# @File     : messages.py
# @Desc     :
import enum


class LoginRequestMsg(object):
    """
    java发送过来的登陆模块消息体参数
    """

    def __init__(self):
        self.requiredIP = ''  # 需要登录的服务器IP
        self.bankCode = ""  # 银行
        self.timestamp = 0  # 时间戳
        self.departmentId = 0  # 部门id
        self.userId = 0  # 用户id
        self.account = ""  # 账户
        self.accountId = 0  # 账户id
        self.loginName = ""  # 登录账户名
        self.passwd = ""  # hex(16进制): 登陆密码-AES(CBC模式)加密后的密码
        self.tradingPassword = ""  # 交易密码
        self.verificationCode = ""  # 验证码
        self.otpBody = 0  # 一次性密码
        self.requestType = 0  # type
        self.firstLogin = 0  # type
        self.serverEventId = 0  # type
        self.requestKey = ''  # 请求key


@enum.unique
class ServerEventIdType(enum.IntEnum):
    """
    需要的服务端事件ID
    """
    UnknownError = -2  # 未知错误
    Other = 0  # 其他
    SendAcctPwd = 1    # 发送登录账号密码
    SendVerification = 2    # 发送验证码
    SendOtp = 3    # 发送otp
    SendImgVerification = 4    # 发送图形验证码
    RefreshVerification = 5  # 请求新的验证码
    RefreshImgVerification = 6  # 请求新的图形验证码
    RefreshOtp = 7  # 请求新的otp
    StartConn = 8  # 启动连接
    CheckOtp = 9  # 切换（大华otp方式切换）