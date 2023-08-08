#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/8 16:23
# @File     : decimal_demo.py
# @Desc     :

def test_round():
    a1 = 1.01
    b1 = 1.02

    if a1+b1 == 2.03:
        print('ok')
    else:
        print('no')
    # 有精度的误差
    print(a1+b1)


def test_round2():
    from decimal import Decimal
    a2 = Decimal('1.01')
    b2 = Decimal('1.02')

    if a2 + b2 == Decimal('2.03'):
        print('ok')
    else:
        print('no')
    print(a2 + b2)
    print(type(a2 + b2))


def test_round3():
    from decimal import Decimal
    result = Decimal(0.123456789).quantize(Decimal("0.0000"))  # quantize：设置小数位数
    print(result)


def test_round4(n, d):
    from decimal import Decimal, getcontext
    getcontext().prec = 5  # 利用getcontext().prec设定有效数字
    result = Decimal(n).quantize(Decimal(d))  # quantize：设置小数位数
    print(result)


def test_round5(n, _format='0.00'):
    from decimal import Decimal
    from decimal import ROUND_HALF_UP, ROUND_HALF_EVEN
    num_1 = Decimal(n).quantize(Decimal(_format), rounding=ROUND_HALF_UP)
    num_2 = str(Decimal(n).quantize(Decimal(_format), rounding=ROUND_HALF_EVEN))
    print(n, num_1, type(num_1), num_2, type(num_2))
    print("\n\n")


def test_round6(n, _format='0.00'):
    from decimal import Decimal, ROUND_HALF_UP
    num_1 = Decimal(n).quantize(Decimal(_format), rounding=ROUND_HALF_UP)
    print(n, num_1, type(num_1))
    print("\n\n")


def test_round7(n, d=0):
    from decimal import Decimal, ROUND_HALF_UP
    if d < 0:
        return n
    elif d == 0:
        _format = '0'
    else:
        _format = '0.' + '0'*d
    num = Decimal(n).quantize(Decimal(_format), rounding=ROUND_HALF_UP)
    print(_format, n, num)
    return num

# test_round()
# test_round2()
# test_round3()
# test_round4(0.123456789, "0.0000")
# test_round4(3.155, "0.0000")
# test_round4(3.155, "0.00")
# test_round5('0.125', '0.00')
# test_round5('0.375', '0.00')
# test_round6(0.315, '0.000')
# test_round6(0.315, '0.00')
# test_round6(0.315, '0.00')
# test_round6(0.315, '0.00')

# test_round7(0.315, 2)
# test_round7(0.316, 2)
test_round7(0.316, 5)
# test_round7(3, -1)


