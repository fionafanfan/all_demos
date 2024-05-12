import itertools
import random


def generate_random_numbers(arr: list, length: int, repeat_limit: int, pre_fix=None, count=120):
    """
    生成车牌号：
    东莞： 前缀固定 -粤S
    东莞： 后缀 - 规则： 5位数； 【纯数字，纯字母， 数字+字母】

    生成随机号码
    :param arr: 可选元素
    :param length: 生成内容的长度
    :param repeat_limit: 重复数字最多出现次数
    :param pre_fix: 固定前缀
    :param count: 生成号码的数量
    """                                                                                                                                                                                                                                                                                
    if pre_fix is None:
        pre_fix = []
    arr = list(map(str, arr))
    pre_fix = list(map(str, pre_fix))
    pool = set(itertools.product(arr, repeat=length - len(pre_fix)))
    result = set()
    while len(result) < count:
        combination = "".join(random.choice(list(pool)))
        if combination.count(combination[0]) > repeat_limit:
            continue
        result.add("".join(pre_fix + list(combination)))
    return result


if __name__ == '__main__':
    nums = [1, 2, 5, 8, 6, 9]
    strs_ = ['F', 'A', 'W']
    choices = nums + strs_
    choices = [2, 9, 'A', 'F', 'N']
    car_nos = generate_random_numbers(arr=choices, length=5, repeat_limit=2, pre_fix=[2], count=20)
    print(car_nos)
