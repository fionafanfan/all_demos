#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/21 14:10
# @File     : dict_collections_defaultdict_dm_one.py
# @Desc     :
from collections import defaultdict

"""
collections 模块中的 defaultdict 类是一个字典的子类，它提供了一个可指定默认值的字典。
主要作用是在字典中访问不存在的键时，不会抛出 KeyError 异常，而是返回一个用户指定的默认值。

1、设置默认值： defaultdict 允许在创建字典时指定一个默认值类型，当访问字典中不存在的键时，该键会被自动初始化为默认值。
2、减少错误： 使用 defaultdict 可以减少在访问字典中不存在的键时引发的错误。这在某些场景下很有用，尤其是在统计或计数数据时。
3、简化代码： 使用 defaultdict 可以使代码更简洁，无需显式检查键是否存在。
总的来说，defaultdict 是一种方便的工具，特别适用于需要处理缺失键的情况。在某些场景下，它可以使代码更清晰、更紧凑。
"""


def demo_one():
    """
    设置默认值： defaultdict 允许在创建字典时指定一个默认值类型，当访问字典中不存在的键时，该键会被自动初始化为默认值。
    :return:
    """
    # 创建一个 defaultdict，指定默认值为 int 类型（默认为0）
    my_dict = defaultdict(int)

    # 访问不存在的键，自动初始化为默认值
    my_dict['a'] += 1
    print(my_dict)  # 输出: defaultdict(<class 'int'>, {'a': 1})


def demo_two():
    """
    减少错误： 使用 defaultdict 可以减少在访问字典中不存在的键时引发的错误。这在某些场景下很有用，尤其是在统计或计数数据时。
    :return:
    """
    word_counts = defaultdict(int)

    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

    # 统计单词出现次数
    for word in words:
        word_counts[word] += 1

    print(word_counts)  # 输出: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})


def demo_two_compare():
    # 使用普通字典
    normal_dict = {}
    key = 'some_key'

    if key in normal_dict:
        normal_dict[key] += 1
    else:
        normal_dict[key] = 1

    # 使用 defaultdict
    defaultdict_example = defaultdict(int)
    defaultdict_example[key] += 1
    print(normal_dict, defaultdict_example)


if __name__ == "__main__":
    demo_one()
    demo_two()
    demo_two_compare()
