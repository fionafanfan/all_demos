#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : taner
# @Date     : 2021/6/23 18:36
# @File     : decorators.py
# @Desc     : decorators

import functools
import time


def _print_no_throw_exception(msg):
    """
    打印时抛出异常
    有时会遇到PermissionError
    """
    try:
        print(msg)
    except Exception:
        pass


def retry(exceptions: list, times=3, wait=1, callback=None, no_throw_exception=False):
    """
    如果抛出指定异常，重试
    :param exceptions: 异常列表
    :param times: 重试次数
    :param wait: 每次重试间隔
    :param callback: 重试之前调用函数对象
    :param no_throw_exception: 最后是否抛出异常
    """
    if not isinstance(exceptions, (list, tuple)):
        new_exceptions = [exceptions]
    else:
        new_exceptions = exceptions

    def inner_retry(func, count, *args, **kwargs):
        if count > times:
            return
        try:
            return func(*args, **kwargs)
        except tuple(new_exceptions) as e:
            if count < times:
                _print_no_throw_exception(f'Raise exception: {e.__class__.__name__}: {str(e)}')
                _print_no_throw_exception(f'Retry again: {func.__name__}')
                if callback is not None and callable(callback):
                    _print_no_throw_exception(f'Retry callback: {callback.__name__}')
                    callback()
                time.sleep(wait)
                return inner_retry(func, count + 1, *args, **kwargs)
            else:
                if not no_throw_exception:
                    raise e
                else:
                    return

    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return inner_retry(func, 0, *args, **kwargs)

        return wrapped

    return decorator


def singleton(cls):
    """
    单例
    """
    _instances = {}

    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return wrapper


def cache(expire=3600, dont_caches=[None, '']):
    """
    缓存
    :param expire: 过期时间
    :param dont_caches: 不缓存的值
    """
    def decorator(func):
        cached = dict()

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            key = '_'.join([str(func.__hash__()), str(args), str(kwargs)])
            nonlocal cached
            value = cached.get(key)
            if not value or time.time() > value['expire'] or value['return'] in dont_caches:
                now = time.time()
                cached = {k: v for k, v in cached.items() if v['expire'] > now}

                func_rtn = func(*args, **kwargs)

                cached[key] = dict()
                cached[key]['return'] = func_rtn
                cached[key]['expire'] = time.time() + expire

            return cached[key]['return']
        return wrapped

    return decorator


def no_throw_exception(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            _print_no_throw_exception(f"Raise exception: {func.__name__}")

    return wrapped
