#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/30 14:55
# @File     : mock_bot_case.py
# @Desc     :
import json
import time

from kafka import KafkaProducer, KafkaConsumer, TopicPartition

bootstrap_servers = '172.16.6.43:9092, 172.16.6.42:9092, 172.16.6.48:9092'


def kafka_producer_login():

    requireIP = "192.168.1.35"  # 192.168.1.35 && 172.16.6.145 && 172.16.6.146
    env_head = "fan_dev"  # kafka topic 环境前缀
    env_suffix = "simulate"

    raw_kafka_topic = {
        "server_args": "default_server_args",
        "logout": "default_logout",
        "trade_cancel_order": f"default_cancel_trade",
        "strategy_trade_order": f"default_strategy_trade",
        "quick_trade_order": f"default_quick_trade",
        "cancel_order": "default_cancel_trade"
    }
    kafka_topic = {k: f"{env_head}_{v}_{env_suffix}" for k, v in raw_kafka_topic.items()}

    bank_infos = {
        "yintou": {
            "bank_code": "InteractiveBrokers",
            "bank_type": 2,  # int 银行类型(2:"InteractiveBrokers")
            "account": "stringlew",  # 盈透登录 需要用子账户登录网关， 用主账户登录网页
            "login_name": "stringlew",  # 盈透的登录网关账号， 配置中有相关配置。
            "account_id": 8319,  # dev: dept_id, account_id = 1000, 8318
            "department_id": 1000,
            "user_id": 101,  # int：用户id
            "password": "fc12fc58d2fd3690325702d82c125ff8",
        },

        "futu": {
            "bank_code": "Futu",
            "bank_type": 5,
            "account": "232499150",
            "login_name": "232499150",  #
            "department_id": 1006,
            "account_id": 450,
            "password": "565533628f5b83c668143bf5cf1acd28"
        }
    }

    bank_list = list(bank_infos.keys())
    while bank_list:
        time.sleep(0.01)
        bank_name = input(f"请输入即将要测试的银行(支持测试的银行有:{bank_list}):")
        if bank_name in bank_infos:
            bank = bank_infos.get(bank_name, {})

            bank_code = bank.get("bank_code", '')
            bank_type = bank.get("bank_type", 0)
            account = bank.get("account", "")
            login_name = bank.get("login_name", "")
            account_id = bank.get("account_id", 0)
            department_id = bank.get("department_id", 0)
            user_id = bank.get("user_id", 0)
            password = bank.get("password", "")
            verification_code = bank.get("verification_code", "")

            messages = {
                '5': {
                    "requiredIP": requireIP,
                    "bankCode": bank_code,
                    "timestamp": 1659683772965,
                    "account": account,
                    "accountId": account_id,
                    "departmentId": department_id,
                    'userId': user_id,
                    "loginName": login_name,
                    "passwd": password,
                    "tradingPassword": "",
                    "verificationCode": "",
                    "otpBody": "",
                    "requestType": 0,
                    "firstLogin": -1,
                    "serverEventId": 5
                },
                '1': {
                    "requiredIP": requireIP,
                    "bankCode": bank_code,
                    "timestamp": 1659683772965,
                    "account": account,
                    "accountId": account_id,
                    "departmentId": department_id,
                    'userId': user_id,
                    "loginName": login_name,
                    "passwd": password,
                    "tradingPassword": "",
                    "verificationCode": "",
                    "otpBody": "",
                    "requestType": 0,
                    "firstLogin": 1,  # 首次登录 初始化流水  其它时候传入，没有用到 如果用到了1的话，手动在数据库中修改会被改回来。
                    "serverEventId": 1  # 发送登录账号
                },
                '2': {
                    "requiredIP": requireIP,
                    "bankCode": bank_code,
                    "timestamp": 1659683772965,
                    "account": account,
                    "accountId": account_id,
                    "departmentId": department_id,
                    'userId': user_id,
                    "loginName": login_name,
                    "passwd": password,
                    "tradingPassword": "",
                    "verificationCode": "4huo",
                    "otpBody": "",
                    "requestType": 4,
                    "firstLogin": -1,
                    "serverEventId": 2  # 发送验证码
                },
                '6': {
                    "requiredIP": requireIP,
                    "bankCode": bank_code,
                    "timestamp": 1659683772965,
                    "account": account,
                    "accountId": account_id,
                    "departmentId": department_id,
                    'userId': user_id,
                    "loginName": "",
                    "passwd": "",
                    "tradingPassword": "",
                    "verificationCode": "",
                    "otpBody": "",
                    "requestType": 4,  # 4-刷新图形验证码  0-不指定 也行
                    "firstLogin": -1,
                    "serverEventId": 6  # 刷新验证码
                },
                '3': {
                    "requiredIP": requireIP,
                    "bankCode": bank_code,
                    "timestamp": 1659683772965,
                    "account": account,   # 新鸿基和盈透特殊
                    "accountId": account_id,
                    "departmentId": department_id,
                    'userId': user_id,
                    "loginName": login_name,
                    "passwd": "",
                    "tradingPassword": "",
                    "verificationCode": "",
                    "otpBody": "xxx",
                    "requestType": 0,  # 填什么无所谓
                    "firstLogin": 0,
                    "serverEventId": 3  # 发送otp
                },
                "logout": {
                    'kafkaMessageId': "",  # string： kafka消息ID
                    'bankCode': bank_code,  # string: 银行代号
                    'accountId': account_id,  # int: 账户id
                    'account': account,  # string: 账户
                    'logoutName': account,  # string: 登出账户名
                    'timestamp': 1660295049334,	 # int: 时间戳
                },
                "holding": {
                      "tradingAcctCashInfos": [
                        {
                          "tradingAccountId": account_id,  # int 银行账户id
                          "bankType": bank_type,  # int 银行类型(5:"Futu", 8:"CITICS")
                          "currencyType": 0  # int 币种类型(0: "港元", 1: "美元", 2: "人民币", 3: "新币")
                        }
                      ],
                      "stockCode": "00700"  # string 股票代码
                    },
                "holding_all": {
                    "tradingAcctCashInfos": [
                        {
                            "tradingAccountId": account_id,  # int 银行账户id
                            "bankType": bank_type,  # int 银行类型(5:"Futu", 8:"CITICS")
                            "currencyType": 0  # int 币种类型(0: "港元", 1: "美元", 2: "人民币", 3: "新币")
                        }
                    ],
                    "stockCode": ""  # string 股票代码
                },
                "statement": {
                    "tradingAccountId": account_id,  # int 银行账户id
                    "bankType": bank_type,  # int 银行类型(5:"Futu", 8:"CITICS") # 富途 没有主动获取流水
                    "ids": ['123', '124']  # list 银行流水id集合
                },
                "state_bal": {
                        "tradingAccountId": account_id,  # int 银行账户id
                        "bankType": bank_type,  # int 银行类型(5:"Futu", 8:"CITICS")
                        "operateUserId": 0,  # 操作用户ID
                    },
                "order_stategy": {
                        "regionType": 1,  # v1.2.130美股机器手迭代新增
                        "kafkaMessageId": "",  # string： kafka消息ID
                        "bankCode": bank_code,  # string: 银行代号
                        "account": account,  # int: 银行账号
                        "accountId": account_id,  # int: 交易账户id
                        "tradingPassword": password,  # string: 交易密码
                        "tradeDirection": 1,  # int：交易方向  0-买 1-卖
                        "tradingPrice": 7.0,  # decimal：交易价格 # 发单价格{order.tradingPrice}小于等于0  废弃
                        "tradingType": 1,  # 下单类型， 0|限价 1|市价 (增)
                        "stockCode": "00017",  # string：股票代码
                        "tradingQuantities": 198,  # int: 交易股数    不能小于0
                        "tradingCommandId": 10013,  # int: 交易指令id  哪里来的？自己定义的吗？
                        "tradingDetailId": 20013,  # int: 交易详情id   哪里来的？自己定义的吗？
                        "time": int(time.time()*1000),  # int: 放单时间戳 毫秒，要是当天的时间戳，毫秒单位
                    },
                "order_quick": {
                    "regionType": 0,  # v1.2.130美股机器手迭代新增
                    "kafkaMessageId": "",  # string： kafka消息ID
                    "bankCode": bank_code,  # string: 银行代号
                    "account": account,  # int: 银行账号
                    "accountId": account_id,  # int: 交易账户id
                    "tradingPassword": password,  # string: 交易密码
                    "tradeDirection": 0,  # int：交易方向  0-买 1-卖
                    "tradingPrice": 0.0,  # decimal：交易价格
                    "tradingType": 0,  # 下单类型， 0|限价 1|市价 (增)
                    "stockCode": "01810",  # string：股票代码
                    "tradingQuantities": 1,  # int: 交易股数
                    "tradingCommandId": 30012,  # int: 交易指令id
                    "tradingDetailId":  40012,  # int: 交易详情id
                    "time": int(time.time()*1000),	 # int: 放单时间戳
                   },
                "cancel_order": {
                    'kafkaMessageId': "",  # string： kafka消息ID
                    'bankCode': bank_code,	 # string: 银行代号
                    'account': account,	 # string: 银行账号
                    'accountId': account_id,	 # int: 交易账户id
                    'regionType': 1,  # 地区类型 -- 新增   int类型   0|  港股市场  1|美股市场
                    'tradingCommandId': 10,  # int: 交易指令id
                    'tradingDetailId': 20,  # int: 交易记录id,
                    'time': int(time.time()*1000),  # int: 发单时间
                }
            }

            while True:
                time.sleep(0.1)
                producer = KafkaProducer(
                    value_serializer=lambda v: json.dumps(v).encode(),
                    bootstrap_servers=bootstrap_servers
                )
                # 发起的kafka指令--登录
                topic = f"{env_head}_default_server_args_{env_suffix}"
                print(f"【{bank_name}】【{env_head}】【{requireIP}】支持的执行步骤:【{list(messages.keys())}】")
                step = input(f"请输入[{bank_name}]执行测试步骤:")
                if step in messages:
                    data = messages.get(step, {})
                    if step == "1":
                        topic = kafka_topic.get("server_args", "")
                    elif step == "2":
                        topic = kafka_topic.get("server_args", "")
                        ver_code = input("请输入验证码:")
                        data['verificationCode'] = ver_code
                        if bank_name in ["yintou"]:
                            data['requestType'] = 3
                    elif step == "3":
                        topic = kafka_topic.get("server_args", "")
                        otp_code = input("请输入保安编码:")
                        data['otpBody'] = otp_code
                    elif step == "logout":
                        # 发起的kafka指令--退出
                        topic = kafka_topic.get("logout", "")
                    elif step == "holding":
                        topic = kafka_topic.get("stock_holding_receive", "")
                    elif step == "holding_all":
                        topic = kafka_topic.get("stock_holding_receive", "")
                    elif step == "statement":
                        topic = kafka_topic.get("bank_statement_receive", "")
                    elif step == "state_bal":
                        topic = kafka_topic.get("bank_statement_balance_receive", "")
                    elif step == "order_stategy":
                        topic = kafka_topic.get("strategy_trade_order", "")
                    elif step == "order_quick":
                        topic = kafka_topic.get("quick_trade_order", "")
                    elif step == "cancel_order":
                        topic = kafka_topic.get("cancel_order", "")

                    print(f"执行的操作:{step} 数据:{data}")
                    producer.send(topic, data)
                    producer.close()
                    print("--end---")
                elif step == "q":
                    print("退出执行程序")
                    break
                else:
                    print("不支持的操作，请重新输入")
        elif bank_name == "q":
            print("退出银行测试")
            break
        else:
            print("输入的银行不存在")


if __name__ == '__main__':
    kafka_producer_login()
