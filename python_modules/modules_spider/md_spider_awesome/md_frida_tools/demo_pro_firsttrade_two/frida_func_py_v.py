#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/7/30 15:13
# @File     : frida_func_py_v.py
# @Desc     :
"""
package f1;

public final class g
{
  public static final String a = String.valueOf('\001');
  public static final String b = String.valueOf('\004');
  public static final String c = String.valueOf('\005');
  public static final String d = String.valueOf('\022');
  public static final String e = String.valueOf('\025');
  public static final String f = String.valueOf('\021');
  public static final String g = String.valueOf('\026');
}

public static String j(String paramString)
    {
    if (!j.y(paramString)) {
      paramString = paramString.replaceAll(f1.g.a, "<SOH>").replaceAll(f1.g.b, "<EOT>").replaceAll(f1.g.c, "<EOH>").replaceAll(f1.g.d, "<EOI>").replaceAll(f1.g.e, "<EOF>").replaceAll(f1.g.f, "<EOB>").replaceAll(f1.g.g, "<EONB>");
    } else {
      paramString = null;
    }
    return paramString;
}
"""


class G:
    A = chr(1)
    B = chr(4)
    C = chr(5)
    D = chr(18)
    E = chr(25)
    F = chr(21)
    G = chr(26)


def replace_special_characters(param_string):
    if not param_string:
        return None

    return (param_string.replace(G.A, "<SOH>")
                        .replace(G.B, "<EOT>")
                        .replace(G.C, "<EOH>")
                        .replace(G.D, "<EOI>")
                        .replace(G.E, "<EOF>")
                        .replace(G.F, "<EOB>")
                        .replace(G.G, "<EONB>"))


def demo_replace_special_characters():
    """
    作用： 将特殊符号打印出来.
    示例1：
    p>5000^0|5110^E4BDBFE794A8E88085202F20E5AF86E7A2BCE98CAFE8AAA4|5010^SEE502|
    r>5000^0|5110^E4BDBFE794A8E88085202F20E5AF86E7A2BCE98CAFE8AAA4|5010^SEE502|

    示例2：
    p>8=FIX.4.335=UQ02142=IH347=tw7800=SE34=0369=0-21474836487030^771589S275^HK7006^0.99553^771589S6050^749499^192.168.1.497800^SE6000^M2RiYjk5YjctMDcxNi00NTM17016^771589S98^
    r>8=FIX.4.3<SOH>35=UQ02<SOH>142=IH<SOH>347=tw<SOH>7800=SE<SOH>34=0<SOH>369=0<SOH><EOB><EOH>-2147483648<EOI>7030^771589S<EOT>275^HK<EOT>7006^0.99<EOT>553^771589S<EOT>6050^74<EOT>9499^192.168.1.49<EOT>7800^SE<EOT>6000^M2RiYjk5YjctMDcxNi00NTM1<EOT>7016^771589S<EOT>98^<EOT><EOB>
    :return:
    """
    p_s = '5000^0|5110^E4BDBFE794A8E88085202F20E5AF86E7A2BCE98CAFE8AAA4|5010^SEE502|'
    # p_s = '8=FIX.4.335=UQ02142=IH347=tw7800=SE34=0369=0-21474836487030^771589S275^HK7006^0.99553^771589S6050^749499^192.168.1.497800^SE6000^M2RiYjk5YjctMDcxNi00NTM17016^771589S98^'
    r_s = replace_special_characters(p_s)
    print(f'p>{p_s}\nr>{r_s}')


# ==========================================


def E(paramArrayOfByte, paramInt1, paramInt2):
    if paramArrayOfByte is not None and len(paramArrayOfByte) > paramInt1:
        j = len(paramArrayOfByte) - paramInt1
        i = j if paramInt2 <= 0 else min(j, paramInt2)
        arrayOfByte = paramArrayOfByte[paramInt1:paramInt1 + i]
        paramArrayOfByte = arrayOfByte
    else:
        paramArrayOfByte = None
    return paramArrayOfByte



def F(paramArrayOfByte, paramInt1, paramInt2):
    paramArrayOfByte = E(paramArrayOfByte, paramInt1, paramInt2)
    if paramArrayOfByte is not None and len(paramArrayOfByte) > 0:
        paramArrayOfByte = paramArrayOfByte.decode('utf-8')
    else:
        paramArrayOfByte = None
    return paramArrayOfByte


def demo_f():
    param_array_of_bype = '82,48,44,49'
    paramInt1, paramInt2 = 0, 0
    r  = F(param_array_of_bype, paramInt1, paramInt2)
    print(f'r: {r}')


def main():
    demo_replace_special_characters()

if __name__ == "__main__":
    main()
