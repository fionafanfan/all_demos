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

            初始化动作：
                定义与使用：
                    初始化浏览器驱动
                    初始化心跳线程
                    初始化是否发送每日余额标记
                    初始化redis消息队列键
                    初始化机器手任务状态

                只定义，在子类中使用：
                    kafka消息主题订阅


        跟流水相关的：
           Bot.on_get_statement
           Bot.sync_statement  同步流水
               self.statement_mgr.sync_statement(*args, **kwargs)   各个机器手子类实现sync_statement方法，即可实现同步流水
           Bot.get_statement  主动获取流水， 再次对照
               self.statement_mgr.pre_check()
               statement = self.statement_mgr.get_statement_by_id_from_db(id_)  每个流水管理器都要实现吗？还是在流水器管理基类中有呢？
               self.statement_mgr.sync_statement(business_type, serial_number)

           Bot.get_statement_balance 主动获取流水与资金
                self.statement_mgr.resp_status = 1
                self.statement_mgr.sync_statement()
                self.statement_mgr.resp_status = 0
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
