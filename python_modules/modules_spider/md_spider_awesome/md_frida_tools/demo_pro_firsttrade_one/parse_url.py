#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/6/3 10:09
# @File     : parse_url.py
# @Desc     :
def demo():
    from urllib.parse import unquote
    """
    http://trade.firstsechk.com/i-trade/streaming/streamLogin?re=1&clm=P678/fO7GPWmD/wpeYdAePFQNoMhC031pTbUsuXSEGpbPZSYvNhvYEdVY2VfDP0quPOH+bXZr2Kp
    uMXd6s38xyrasInrP2EQaoOyp7LRoJRNbpBNg4AoMzQQ70Hfv1YAMkrqOqx4KOOQp0tcienXQf7s
    cgB26zKfry5wqOWVW5tjGtstaNlIMfejJUGfpo/BlqXzLDIYMFT+hWCdZZ7L/sQA7QySw+OzAtgm
    wfsQE5nRS8QDkiZPYc4eWDz1Rp2909Rtrcg+243ZPrj9mIQS/KCayyF6E4Oko/lBNfmQSai7sQva
    4FJMFbj3OnYyEYrYyEJhffgQPbSWs2GsMMfsi0lrTB/qyM/97o8DznRKRp4W1664wAoeuotkqKvE
    lj3FWv/2mdnLrliLBk343rsrn/+NkU2Sett0gAWV8r0Fpu9E88l8RU7PX7AR3Dg5+5+BBvDOmB/A
    RTKxbinjVuLGMwYa5v1+JNBj91pPjoYStxwGs+3E+cIhm4fWYMdRQC8xo62DT0F1wkXjm2zgasZy
    lMWrIb3iUCOhfq0H81dqQQLWP/kAbQpOVY/GhfhGIfrBImY76JET6TwbkKr9Dw18sVdWCz8KKNJe
    mcXj/+XfdSGAJDmvq+ZKRe8p6S4XQw4kBvXUOG3zu6/RgnfPektpVxfpFRsPzO2AH3dUIQv9jVs=
    """
    url = 'http://trade.firstsechk.com/i-trade/streaming/streamLogin?re=1&clm=P678%2FfO7GPWmD%2FwpeYdAePFQNoMhC031pTbUsuXSEGpbPZSYvNhvYEdVY2VfDP0quPOH%2BbXZr2Kp%0AuMXd6s38xyrasInrP2EQaoOyp7LRoJRNbpBNg4AoMzQQ70Hfv1YAMkrqOqx4KOOQp0tcienXQf7s%0AcgB26zKfry5wqOWVW5tjGtstaNlIMfejJUGfpo%2FBlqXzLDIYMFT%2BhWCdZZ7L%2FsQA7QySw%2BOzAtgm%0AwfsQE5nRS8QDkiZPYc4eWDz1Rp2909Rtrcg%2B243ZPrj9mIQS%2FKCayyF6E4Oko%2FlBNfmQSai7sQva%0A4FJMFbj3OnYyEYrYyEJhffgQPbSWs2GsMMfsi0lrTB%2FqyM%2F97o8DznRKRp4W1664wAoeuotkqKvE%0Alj3FWv%2F2mdnLrliLBk343rsrn%2F%2BNkU2Sett0gAWV8r0Fpu9E88l8RU7PX7AR3Dg5%2B5%2BBBvDOmB%2FA%0ARTKxbinjVuLGMwYa5v1%2BJNBj91pPjoYStxwGs%2B3E%2BcIhm4fWYMdRQC8xo62DT0F1wkXjm2zgasZy%0AlMWrIb3iUCOhfq0H81dqQQLWP%2FkAbQpOVY%2FGhfhGIfrBImY76JET6TwbkKr9Dw18sVdWCz8KKNJe%0AmcXj%2F%2BXfdSGAJDmvq%2BZKRe8p6S4XQw4kBvXUOG3zu6%2FRgnfPektpVxfpFRsPzO2AH3dUIQv9jVs%3D%0A'
    d = unquote(url)
    print(d)


def demo_one(input_array):
    """
     固定的整数数组转成字节数组， 再转base64字符串， 这个base64是固定的。
    param: input_array: 字节数组 [-60, 113, 27, 12, 97, 111, -12, -39]
    Encoded String: xHEbDGFv9Nk=
    :return:
    """
    import base64

    # 将整数数组转换为字节数组
    byte_array = bytearray((x & 0xff) for x in input_array)

    # Base64编码
    encoded_str = base64.b64encode(byte_array).decode('utf-8')

    return encoded_str


# 输入的整数数组
def test_demo_one():
    """
    [android.support.v4.media.f.q] param=-60,113,27,12,97,111,-12,-39
    [*] [-60, 113, 27, 12, 97, 111, -12, -39]
    [android.support.v4.media.f.q] result=xHEbDGFv9Nk=

    [android.support.v4.media.f.q] param=-22,19,1,-10,113,52,-126,-10,82,-87,127,43,-112,107,-68,-72,12,84,48,42,19,19,105,112,72,12,104,121,81,-120,-112,-72,-52,-85,86,-31,-16,-75,-78,-40,57,-16,117,48,-40,-94,65,-37,24,-124,-118,-76,114,-111,30,29,113,-80,-79,112,85,67,58,88,-39,108,-16,-114,54,-31,-27,51,-120,70,12,125,-124,122,122,115,-82,27,-1,-49,-127,11,69,-54,66,60,-24,30,-57,-47,109,19,66,19,106,-98,-49,28,73,-97,-40,48,-118,-5,-71,-12,112,5,-80,59,100,-29,-15,95,60,-128,83,63,-114,-36,-90,-124,101,-96,59,-10,58,49,-47,-41,126,-75,27,-71,73,-127,-99,-126,56,75,-80,107,-53,-81,33,7,-114,89,107,116,81,-46,-128,34,-3,111
    [*] [-22, 19, 1, -10, 113, 52, -126, -10, 82, -87, 127, 43, -112, 107, -68, -72, 12, 84, 48, 42, 19, 19, 105, 112, 72, 12, 104, 121, 81, -120, -112, -72, -52, -85, 86, -31, -16, -75, -78, -40, 57, -16, 117, 48, -40, -94, 65, -37, 24, -124, -118, -76, 114, -111, 30, 29, 113, -80, -79, 112, 85, 67, 58, 88, -39, 108, -16, -114, 54, -31, -27, 51, -120, 70, 12, 125, -124, 122, 122, 115, -82, 27, -1, -49, -127, 11, 69, -54, 66, 60, -24, 30, -57, -47, 109, 19, 66, 19, 106, -98, -49, 28, 73, -97, -40, 48, -118, -5, -71, -12, 112, 5, -80, 59, 100, -29, -15, 95, 60, -128, 83, 63, -114, -36, -90, -124, 101, -96, 59, -10, 58, 49, -47, -41, 126, -75, 27, -71, 73, -127, -99, -126, 56, 75, -80, 107, -53, -81, 33, 7, -114, 89, 107, 116, 81, -46, -128, 34, -3, 111]
    [android.support.v4.media.f.q] result=6hMB9nE0gvZSqX8rkGu8uAxUMCoTE2lwSAxoeVGIkLjMq1bh8LWy2DnwdTDYokHbGISKtHKRHh1x
    sLFwVUM6WNls8I424eUziEYMfYR6enOuG//PgQtFykI86B7H0W0TQhNqns8cSZ/YMIr7ufRwBbA7
    ZOPxXzyAUz+O3KaEZaA79jox0dd+tRu5SYGdgjhLsGvLryEHjllrdFHSgCL9bw==

    :return:
    """
    input_array = [-60, 113, 27, 12, 97, 111, -12, -39]
    expect_str = "xHEbDGFv9Nk="

    input_array = [-22, 19, 1, -10, 113, 52, -126, -10, 82, -87, 127, 43, -112, 107, -68, -72, 12, 84, 48, 42, 19, 19, 105, 112, 72, 12, 104, 121, 81, -120, -112, -72, -52, -85, 86, -31, -16, -75, -78, -40, 57, -16, 117, 48, -40, -94, 65, -37, 24, -124, -118, -76, 114, -111, 30, 29, 113, -80, -79, 112, 85, 67, 58, 88, -39, 108, -16, -114, 54, -31, -27, 51, -120, 70, 12, 125, -124, 122, 122, 115, -82, 27, -1, -49, -127, 11, 69, -54, 66, 60, -24, 30, -57, -47, 109, 19, 66, 19, 106, -98, -49, 28, 73, -97, -40, 48, -118, -5, -71, -12, 112, 5, -80, 59, 100, -29, -15, 95, 60, -128, 83, 63, -114, -36, -90, -124, 101, -96, 59, -10, 58, 49, -47, -41, 126, -75, 27, -71, 73, -127, -99, -126, 56, 75, -80, 107, -53, -81, 33, 7, -114, 89, 107, 116, 81, -46, -128, 34, -3, 111]
    expect_str = "6hMB9nE0gvZSqX8rkGu8uAxUMCoTE2lwSAxoeVGIkLjMq1bh8LWy2DnwdTDYokHbGISKtHKRHh1xsLFwVUM6WNls8I424eUziEYMfYR6enOuG//PgQtFykI86B7H0W0TQhNqns8cSZ/YMIr7ufRwBbA7ZOPxXzyAUz+O3KaEZaA79jox0dd+tRu5SYGdgjhLsGvLryEHjllrdFHSgCL9bw=="
    encoded_str = demo_one(input_array)
    print("Encoded String:", encoded_str, '对比结果:', encoded_str==expect_str)


if __name__ == '__mian__':
    test_demo_one()

