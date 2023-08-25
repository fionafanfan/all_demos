#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/23 9:48
# @File     : io_string.py
# @Desc     :


def demo_one():
    import io

    s = "hello, world"

    sio = io.StringIO(s)
    print(type(sio), dir(sio), sio.getvalue())
    print(sio.seek(7))
    sio.write("there!")
    print(sio.getvalue())


def demo_two():
    import array
    s = "hello, world"
    a = array.array('u', s)
    print(a)
    a[0] = 'y'
    print(dir(a))
    print(a.tounicode())


if __name__ == "__main__":
    # demo_one()
    demo_two()


