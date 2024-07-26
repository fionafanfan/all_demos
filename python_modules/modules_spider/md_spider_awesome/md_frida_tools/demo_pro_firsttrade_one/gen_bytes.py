#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/6/3 14:15
# @File     : gen_bytes.py
# @Desc     : 将数值列表生成十六进制字节

def gen_data(ddt):
    # dt = 'fa415f14fdea9ac5'
    dt = ddt
    print(len(dt))
    dtt = []
    for i in range(int(len(dt)/2)):
        # print(i)
        ds = '0x' + dt[0] + dt[1]
        dtt.append(ds)
        dt = dt[2:]
        # print(i, dtt, dt)
    print(dtt)
    data = ', '.join([f'(byte) {d}' for d in dtt])
    ds = '{' + data + '}'
    dss = f'new byte[]{ds}'
    print(dss)


def gen_data2(dt):
    # dt = [51, 53, 61, 83, 85, 48, -55, 1]
    print(len(dt))
    data = ', '.join([f'(byte) {d}' for d in dt])
    ds = '{' + data + '}'
    dss = f'new byte[]{ds}'
    print(dss)


# dt = [64, -32, -81, -120, 110, 80, -68, 123, -61, 44, -120, -97, 72, -54, -73, 14, -25, 108, -90, 38, 58, 75, -49,
#       -25, 124, -112, -35, 20, -113, -18, -127, 78, -49, 35, -21, 62, 45, 99, 58, -83, -20, 55, 18, -128, 42, 120,
#       -43, 0, -59, -95, -26, 32, 27, -33, -98, 65, 103, -37, -116, 41, -107, 78, -15, 48, 47, 100, -23, 32, 47, 93,
#       -92, 106, -70, 16, -72, 91, 123, 123, 47, 55, 28, -7, -122, 88, -3, -92, 46, -94, 24, -79, -110, 107, -124,
#       72, -10, -118, -113, -50, 36, -119, -87, 87, -119, -109, -114, -61, -2, 25, 71, 117, -48, 29, -115, -49, 91,
#       -50, 66, -31, 43, -9, -1, -64, 120, -54, 57, -112, 125, -21, 28, -67, -96, -24, 43, 97, 65, 115, -10, 127,
#       -92, -63, 12, 47, -74, -54, 54, 33, -101, -9, -71, 91, 109, -89, -19, -5, 100, 89, 50, -44, -119, -11, 67,
#       126, -4, -34, -45, 0, -57, 9, -16, -115, 104, -13, -75, -104, -12, -67, 18, -50, 68, -118, 100, -118, 89, -4,
#       -7, -41, 76, -108, -126, 88, -29, -113]

ddt = 'fa415f14fdea9ac5'
# dt = [51,53,61,83,85,48,55,1,21,5,45,50,49,52,55,52,56,51,54,52,56,18,57,54,49,51,94,56,4,53,50,55,54,94,83,69,72,75,4,55,48,55,54,94,78,65,83,68,4,57,54,49,55,94,48,54,47,48,51,47,50,48,50,52,32,48,48,58,48,48,58,48,48,48,4,53,55,52,94,48,49,4,21,17]
dt = [51,53,61,83,85,57,51,1,21,5,45,50,49,52,55,52,56,51,54,52,56,18,21,17]

# # ip地址
# ddt = 'e6b82e81b1c84ec6'
# dt = [-119,-99,121,107,-14,49,63,12,5,118,1,40,-55,33,83,-38]
#
# # 密码
# ddt = '2ae301ee686c6915'
# dt = [-13,-27,93,93,24,-55,81,-76]

# 771589S
# YzUwZWIyMTctOWZkMi00OGM4771589S
# firstsectrade

ddt = 'b89c9946cd50f68f'
dt = [49, -8, -36, 89, -125, 13, -18, 32]
gen_data(ddt)
gen_data2(dt)


