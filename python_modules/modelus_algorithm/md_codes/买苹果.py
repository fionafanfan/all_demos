#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : fionafan
# @Date     : 2023/2/24 15:32
# @File     : 买苹果.py
# @Desc     :

class Solution:
    def __init__(self) -> None:
        """
        6x + 8y = n
        min(x+y)
        """
        pass

    def solution(self, n):
        result = -1

        # TODO: 请在此编写代码  y 代买 8 个装 买几袋
        for y in range(18):
            m = divmod((n - 2*y), 6)
            s = m[0]
            x = s - y
            if s >= 0 and x >= 0 and y >= 0 and 6*x + 8*y == n:
                print(f"s:{s}  x:{x} y:{y}  6*{x} + 8*{y} == {6 * x + 8 * y}  输入n:{n}")
                if result == -1 or s < result:
                    result = s
        print(f"result:{result}")
        return result


if __name__ == "__main__":
    while True:
        n = int(input("请输入:").strip())

        sol = Solution()
        result = sol.solution(n)
        print(result)

