#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/4 16:23
# @File     : bot.py
# @Desc     :


import abc


class BaseBot(abc.ABC):
    """
    基类
    """

    def __init__(self):
        pass


class BaseAbcBot(BaseBot):
    """
    跟业务相关的有抽象方法的BaseAbcBot基类
    """

    def __init__(self):
        super(BaseAbcBot, self).__init__()

    @classmethod
    @abc.abstractmethod
    def support_bank_code(cls):
        """
        支持的银行代码
        """

    @property
    @abc.abstractmethod
    def bank_code(self):
        pass

    @property
    @abc.abstractmethod
    def bank_type(self):
        pass

    @property
    @abc.abstractmethod
    def account(self):
        pass

    @property
    @abc.abstractmethod
    def order_mgr(self):
        """
        订单管理器
        """
        pass

    @property
    @abc.abstractmethod
    def position_mgr(self):
        """
        持仓管理器
        """
        pass

    @property
    @abc.abstractmethod
    def statement_mgr(self):
        """
        流水管理器
        """
        pass

    @property
    @abc.abstractmethod
    def market(self):
        """
        市场
        """
        pass

    @property
    @abc.abstractmethod
    def max_order(self):
        """
        最大订单数
        """
        pass

    @abc.abstractmethod
    def on_boot(self):
        """
        启动检查
        """
        pass


class Bot(BaseBot, BaseAbcBot):
    """
    机器手基类
        依赖工具：
            selenium + chrome
            kafka
            redis
            定时器
        执行操作：
            初始化心跳线程
            初始化浏览器驱动
            kafka消息主题订阅
            初始化是否发送每日余额标记
            初始化redis消息队列键
            初始化机器手任务状态

    """
    ACCOUNT_ID = 412

    def __init__(self):
        super(Bot, self).__init__()
        self._id = ''

    @property
    def id(self):
        """
        机器手唯一id
        """
        return self._id

    @property
    def account_id(self):
        return self.ACCOUNT_ID
