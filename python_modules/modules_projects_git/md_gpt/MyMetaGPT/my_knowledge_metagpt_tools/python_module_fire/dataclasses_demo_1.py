#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/30 15:03
# @File     : dataclasses_demo_1.py
# @Desc     :
from dataclasses import dataclass

""""
dataclasses 是 Python 3.7 引入的一个标准库，用于简化创建简单类的过程。
它通过使用装饰器来自动添加一些常见的特殊方法，从而减少了需要手动编写的样板代码。

以下是一个简单的示例，演示如何使用 dataclasses：

在上面的例子中，@dataclass 装饰器自动为 Point 类添加了__init__、__repr__ 和 __eq__ 方法，
使其更易于使用。

dataclasses 还提供了其他选项，例如通过 frozen=True 参数创建不可变的数据类，
以及通过 default 参数设置默认值等。

要使用 dataclasses，确保你的 Python 版本在 3.7 或更高。一般情况下，如果你有简单的数据容器类，
并且不想编写繁琐的特殊方法，dataclasses 是一个非常方便的选择。
"""


@dataclass
class Point:
    x: float
    y: float


# 创建 Point 实例
p = Point(1.5, 2.5)


# 自动添加的特殊方法
print(p)  # 输出: Point(x=1.5, y=2.5)
print(repr(p))  # 输出: Point(x=1.5, y=2.5)
print(p == Point(1.5, 2.5))  # 输出: True
