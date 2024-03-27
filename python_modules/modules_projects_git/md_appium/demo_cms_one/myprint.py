#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/9 17:25
# @File     : myprint.py
# @Desc     :


class MyLog(object):

    def __init__(self, last_time=0):
        self.last_ts = last_time

    def myprint(self, s):
        from datetime import datetime
        now = datetime.now()
        cur_time = now.strftime('%Y/%m/%d %H:%M:%S.%f')

        now_timestamp = int(now.timestamp())*1000  # 毫秒
        sub_time = (now_timestamp - self.last_ts)

        if self.last_ts:
            print(f'【{cur_time}】【秒差:{sub_time}】_{s}')
        else:
            print(f'【{cur_time}】【】_{s}')
        self.last_ts = now_timestamp  # 把当前值置为之前的值


if __name__ == '__main__':
    mylog = MyLog()

    mylog.myprint('--- begin ---')
    mylog.myprint('--- 1 ---')
    mylog.myprint('--- 2 ---')
    mylog.myprint('--- end ---')
