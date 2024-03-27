#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/29 18:59
# @File     : fire_demo_1.py
# @Desc     :
"""
fire 是一个 Python 库，由 Google 开发，用于将命令行界面 (CLI) 转换为 Python 对象。
它的目标是使创建命令行界面变得非常简单。通过 fire，你可以将一个 Python 类或模块转换成一个
命令行工具，而无需编写繁琐的解析代码。

以下是一个简单的示例，演示了如何使用 fire 创建一个命令行工具：
在这个例子中，Calculator 类中的 add 和 multiply 方法可以通过命令行调用。例如：
python fire_demo_1.py add 3 5
这将输出 8，表示调用了 add 方法并传递了参数 3 和 5。
fire 还可以用于将函数转换为命令行接口，而不仅仅是类。你可以在需要创建命令行工具的地方使用它，以简化用户与你的代码的交互
"""
import fire


class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


if __name__ == '__main__':
    fire.Fire(Calculator)
