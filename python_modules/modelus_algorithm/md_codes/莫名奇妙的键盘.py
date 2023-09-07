#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : fionafan
# @Date     : 2023/2/24 18:30
# @File     : 莫名奇妙的键盘.py
# @Desc     :

class Solution:
    def __init__(self) -> None:
        """
        有一个神奇的键盘，你可以用它输入a到z的字符，然而每当你输入一个元音字母(a,e,i,o,u其中之一)的时候，
        已输入的字符串会发生一次反转！ 比方说，当前输入了tw，此时再输入一个o，此时屏幕上的字符串two会反转成owt。
        现给出一个字符串，若用该键盘输入，有多少种方法可以得到？

        一行一个字符串，长度不超过200，全部是由小写字母组成。

        一个整数，代表方案数量

        ac

        2
        """
        pass

    def solution(self, str_):
        result = None

        # TODO: 请在此编写代码
        str_list = ['a', 'e', 'i', 'o', 'u']
        if 0 < len(str_) <= 200:
            pass

        return result


if __name__ == "__main__":
    str_ = input("请输入:").strip()

    sol = Solution()
    result = sol.solution(str_)
    print(result)
