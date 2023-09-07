#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : fionafan
# @Date     : 2023/2/23 18:26
# @File     : yinbg.py
# @Desc     :


# 请关闭中文输入法，用英文的字母和标点符号。
# 如果你想运行系统测试用例，请点击【执行代码】按钮，如果你想提交作答结果，请点击【提交】按钮，
# 注意：除答案外，请不要打印其他任何多余的字符，以免影响结果验证
# 本OJ系统是基于 OxCoder 技术开发，网址：www.oxcoder.com
# 模版代码提供基本的输入输出框架，可按个人代码习惯修改

class Solution:
    """
    解题思路：
    不想被找零:
    attr = [1, 2, 8, 16]
    m = 31  不超过m元的商品, 是指1-31元所有的结果 都可以满足
    n = 5
    m = map(n/x, attr)
    x = x1 + x2 + x3 ；令 x值 最小

    demo1:
    1 1
    1
    ret = 1

    demo2:
    1 2
    1
    ret = None

    demo3:
    3 2
    3
    ret = None
    """

    def __init__(self) -> None:
        pass

    def solution1(self, n, m, arr):
        result = None

        # TODO: 请在此编写代码

        if len(arr) != n or n <= 0 or m <= 0:
            result = 'No answer!!!'  # 输入不符合规范
        else:
            moneys = sorted(arr, reverse=False)  # 将币值按从小到大排列
            if m == 1:
                if moneys[0] != 1:
                    result = 'No answer!!!'
                else:
                    result = 1
            else:
                for ni in range(1, n + 1):
                    for mi in range(1, m + 1):
                        print(f"ni:{ni} mi:{mi}")

        return result

    def solution(self, n, m, arr):
        from itertools import combinations

        n, m = arr, m

        max_num = len(n)

        m_range = {i: 0 for i in range(1, m + 1)}

        def inner():

            def is_fill_full():
                return all(m_range.values())

            def fill(nnum):
                for c in combinations(n, nnum):
                    for i in range(1, len(c) + 1):
                        cc = combinations(c, i)
                        for ccc in cc:
                            s = sum(ccc)
                            if s in m_range:
                                m_range[s] = 1
                            if is_fill_full():
                                print('done')
                                return True
                return False

            for i in range(1, max_num + 1):
                print(f'{i} of {max_num}')
                if fill(i):
                    return i

            return 'No answer!!!'

        print(inner())


if __name__ == "__main__":
    # input_1 = "5 31"
    # input_2 = "1 2 8 4 16"

    input_1 = input("请输入行一值:")
    input_2 = input("请输入行二值:")

    arr_temp = [int(item) for item in input_1.strip().split()]

    n = int(arr_temp[0])
    m = int(arr_temp[1])

    arr = [int(item) for item in input_2.strip().split()]

    sol = Solution()
    result = sol.solution(n, m, arr)

    print(result)


