#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/7/29 11:53
# @File     : thread_mgr.py
# @Desc     :
import threading
import time
import traceback
import sys


class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.throw_exception = kwargs['kwargs'].pop('throw_exception', False)
        self.is_db_thread_safe = kwargs['kwargs'].pop('is_db_thread_safe', False)

        self._callable_target = kwargs['target']
        self._args = kwargs['args']
        self._kwargs = kwargs['kwargs']

        self._flag = threading.Event()
        self._flag.set()

        self.exit_code = 0
        self.exception = None
        self.exc_traceback = ''

    def pause(self):
        self._flag.clear()

    def resume(self):
        self._flag.set()

    def wait(self):
        self._flag.wait()

    def run(self):
        try:
            if self._callable_target:
                self._callable_target(*self._args, **self._kwargs)
        except Exception as e:
            self.exception = e
            self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))
            self.exit_code = -1

            print(f"本线程[{self.name}-{self.ident}]发生以下异常")
            print(self.exc_traceback)


class BaseMgr(object):
    def __init__(self):
        self.memory = {}
        self.t = None

    def get(self, name):
        return self.memory.get(name)

    def add(self, name, t):
        self.memory[name] = t
        self.t = t


class ThreadMgr(BaseMgr):
    def __init__(self):
        super().__init__()
        self._main_thread_id = threading.current_thread().ident
        self.is_trading = False
        self.memory = {}

    @property
    def main_thread_id(self):
        return self._main_thread_id

    def pause(self, name):
        t = self.get(name)
        if t:
            self.t.pause()

    def resume(self, name):
        t = self.get(name)
        if t:
            self.t.resume()

    def wait(self, name):
        t = self.get(name)
        if t:
            self.t.wait()

    def add(self, name, target, args=(), register=True, **kwargs):
        if self.get(name):
            print(f"已经存在名为{name}的线程")
            return self.get(name)

        t = MyThread(target=target, args=args, name=name, kwargs=kwargs)
        t.daemon = True
        t.start()

        if register:
            super().add(name, t)

        return t


gThreadMgr = ThreadMgr()


def use_g_thread_mgr_demo_one():
    def listen_std_out():
        for i in range(100):
            print(f'输入文本：{i}')

    gThreadMgr.add(name="Thread_listen_std_out", target=listen_std_out, register=False)

    while True:
        time.sleep(0.5)


if __name__ == '__main__':
    use_g_thread_mgr_demo_one()

