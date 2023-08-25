#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/21 17:48
# @File     : demo_var.py
# @Desc     :
"""
global: 全局变量声明  ； 用于警示副作用的有效性
nonlogcal:

变量：
声明
引用

局部
全局
"""
x = 10


def funca():
    # 函数内部只作引用的 Python 变量隐式视为全局变量, 此时的x 隐式视为全局变量
    #  只是打印， 不会报错
    print(x)


def foo():
    # 如果在函数内部任何位置为变量赋值， 没有明确声明为全局变量， 则默认将其视为局部变量。
    print(x)  # 变为局部变量时， 这个时候就会报错。
    x += 1  # 函数内部对外部变量x 分配了一个新值，所以此时x变为局部变量，


def foo2():
    # 如果在函数内部任何位置为变量赋值， 有明确声明为全局变量， 则将其视为全局变量。
    global x  # 明确声明为全局变量
    print(x)
    x += 1  # 函数内部对外部变量x 分配了一个新值，所以此时x变为局部变量，


def foo3():
    y = 10

    def bar():
        nonlocal y
        print(y)
        y += 1
    bar()
    print(y)


def foo4():
    squares = [lambda: x**2 for x in range(5)]
    print(squares)
    print(squares[2]())
    print(squares[4]())


def foo5():
    squares = []
    for x in range(5):
        squares.append(lambda: x**2)
    print(squares)
    print(squares[2](), type(squares[2]))  # 16 <class 'function'>
    print(squares[4]())  # 16
    x = 8
    print(squares[4]())  # 64


def foo6():
    squares = [lambda n=x:n**2 for x in range(5)]
    print(squares)
    print(squares[2]())
    print(squares[4]())


def foo7():
    squares = [lambda x:x**2 for x in range(5)]
    print(squares)
    print(squares[2](5))
    print(squares[4](6))


def foo8(a, b, /, c):
    print("c", c)
    return a // b, a % b


if __name__ == '__main__':
    # funca()
    # foo()
    # foo2()
    # foo3()
    # foo4()
    # foo5()
    # foo6()
    # foo7()
    print(foo8(3, 2, 1))
    print(foo8(3, 2, c=1))
    # print(foo8(a=3, b=2))
    # divmod(2, 3)

