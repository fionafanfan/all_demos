#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/29 14:06
# @File     : order_mgr.py
# @Desc     :  订单管理器

class OrderMgr(object):

    def __init__(self):
        pass

    def get_stock_config_for_code(self):
        """
        查询账户下股票的配置状态
        SELECT * FROM `t_robot_operation_order_config`  WHERE `account_id` = {account_id} AND `stock_code` = {stock_code}
        :return:
        """
        pass

    def trade_state_map(self):
        """
        银行状态转换为内部订单状态
        银行状态转换为内部订单状态
        :return:
        """
        pass

    def get_orders(self, all_order_info, bot_uid):
        """
        根据bot uid获取其所有订单列表
        :param all_order_info:
        :param bot_uid:
        :return:
        """
        order_info = all_order_info.get(bot_uid, {})
        order_list = order_info.get('tradeDetail', [])
        return order_list