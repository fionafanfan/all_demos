#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/29 11:48
# @File     : stock_trade.py
# @Desc     : stock trade
from biz import messages


def _split_stock_code(code):
    """
    分割股票代码为代码与市场, 兼容港股、美股
    港股: 00700、00700.hk
    美股: AAPL、 AAPL.us

    return: code, market
    """
    results = code.split('.')
    if len(results) > 1:
        return ''.join(results[:-1]), results[-1]
    return results[0], ''


class Bot(object):
    """
    港股美股兼容修改：
    模拟机器手全局定时重启，由原先的的22：00改为早上6点 兼容美股时间。 --待在服务器上的定时管理器中修改。


    下单：
    request topic msg:
    加一个"regionType"参数表示地区类型  -- 已修改

    return topic msg:
    加一个"regionType"参数表示地区类型


    消费订单记录（待需求澄清确认）：acct:{bank_code}:{account_id}:consume:orderSum
    -------------
    下单：
    消费订单数：
       生成消息订单总数key
       初始化消费订单数
       增加一笔记录数
    """

    def __init__(self):
        self.trade_order_msg = messages.ServerTradeOrderMsg()

    def init(self):
        pass

    def can_trade(self):
        """
        当前时间是否可交易
        real_hk_market_open_time = '09:00'
        real_hk_market_close_time = '16:00'

        模拟机器手设置为全天24小时可以交易 , 港股、美股 兼容
        market_open_time = '00:00'
        market_close_time = '23:59'
        :return:
        """

    def stock_trade_common_check(self):
        """
        下单基本检查
        :return:
        """
        messages = ["该订单已发过",
                    "发单数量小于等于0",
                    "发单价格小于等于0",
                    "当前时间不在交易时间内",  # 港美股交易时间兼容
                    "传入的放单时间不在交易时间内",  # 港美股交易时间兼容
                    "该订单在撤单队列中, 无需下单"
                    ]

    def stock_trade(self, requests):
        """
        下单： 快捷交易/策略交易
        :param requests:
        :return:
        1、 return
        2、 trade_Status
        """
        stock_status = [
            "根据特定的股票返回响应的状态",
            "如果股票代码在下面列表中，则直接返回，不做任何处理, settings.ABANDON_CODE",
            "是交易前需要撤单的股票: settings.BEFORE_SELL_TRADE_CANCEL, 未交易之前的撤单情景下，这些股票不做交易，等待撤单时进行状态分配, settings.BEFORE_TRADE_CANCEL",
            "买入返回全部成交的股票&卖出返回等待成交的股票，要求不需要流转",
            "只返回全部成交状态的股票",
            "只返回部分成交状态的股票",
            "只返回等待成交状态的股票",
            "先返回等待成交后再流转成全部成交",
            "先返回等待成交后再流转成放单失败",
            "先返回部分成交后再流转成全部成交",
            "只返回未成交状态的股票",
            "只返回新增且后续撤单只返回未成交或撤单",
            "只返回放单失败",
            "同时返回部分与全部成交",
            "只返回等待成交且撤单不返回任何信息",
            "返回三次撤单失败消息",
            "一个指令生成多个订单状态",
            "卖不做处理",
            "返回放单失败",
            "返回买超失败",
            "返回卖超失败",
            "等待撤单时先返回全部成交后返回撤单失败",
            "返回拒单(延迟两分钟返回)",
            "随机状态"

        ]
        # 订单后续操作:
        # & 构建交易指令中的即时交易信息  bankCode + trade_status + trade_date
        # & 将即时交易信息中的字段更新到本地内存（类）记下来
        # & 构建交易指令中的交易费率信息
        # & 构建成交信息
        # & 如果有成交，将交易费率信息中的字段更新到本地内存
        """
        self.memory_trade_info = {}  交易记录容器
        # 状态流转之前的订单
        part_2_all_orders = self.status_change(uid)
            
        build_real_time_trade_info
        trade_info["marketType"] = MarketType.HK.name  str类型
        填充交易信息:fill_trade_info_fields
        更新到内存（BotRealTimeInfoMsg）：self.trade_info_msg.market = trade_info["marketType"]
        构建交易费用: build_trade_fee_info 全部成交 + 部分成交
        real_time_trade_info["marketType"] = gOrderMgr.parse_to_standard_type('market', self.trade_info_msg.market).value
        
                resp = Response(key=utils.config("trade_infos"),
                        msg=self.memory_trade_info[uid],
                        where=ResponseMsgWay.KafkaQueue)
                        
        生成废弃订单消息响应gen_abandoned_order_response
        real_time_info = self.build_real_time_trade_info(self.trade_order_msg.bankCode, order_status, trade_date)
        构建交易指令中的即时交易信息
        real_time_info = self.build_real_time_trade_info(self.trade_order_msg.bankCode, trade_status, trade_date)
        交易前撤单，返回给kafka的交易状态before_trade_cancel
        real_time_info = self.build_real_time_trade_info(self.trade_cancel_msg.bankCode, trade_status, cancel_date)
        
        回单：
        正常状态下的流转订单
        废弃订单
        撤销订单
        
        """

    def status_change(self, uid, stock_code_=''):
        """
        所有订单状态流转
        :param uid:
        :param stock_code_: 如果提供，只流转指定股票
        :return:
        """
        pass

    def init_order_mem_info(self):
        """
        初始化账户订单信息
        :return:
        """
        pass

    def gen_abandoned_order_response(self):
        """
        生成废弃订单消息响应
        :return:
        """
        pass

    def gen_cancel_fail_order_response(self):
        """
        生成撤单失败消息响应
        :return:
        """
        pass

    def update_trade_order(self, msg_trade):
        self.trade_order_msg.stockCode = _split_stock_code(msg_trade["stockCode"])[0]
        self.trade_order_msg.regionType = int(msg_trade['regionType'])
