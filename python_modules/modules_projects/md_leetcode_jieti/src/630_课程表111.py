#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/12 10:52
# @File     : 630_课程表111.py
# @Desc     : 课程表III
"""
原题：

这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。

你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。

返回你最多可以修读的课程数目。



示例 1：

输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出：3
解释：
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
示例 2：

输入：courses = [[1,2]]
输出：1
示例 3：

输入：courses = [[3,2],[4,3]]
输出：0


提示:

1 <= courses.length <= 104
1 <= durationi, lastDayi <= 104


思路详解：
课程表， 这奇怪的题目， 之前都没有做过
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
看这个示例，应该是按课程需要的天数， 正序排序的。
去除一些不合理的课程数据， 如结束的日期，居然小于 需要的天数， 这显然不合理。
100  101
101+200   301
301+ 1000  1301> 1250
则这门课就不能上了， 需要的最晚日期是1301， 而实际要求是1250 ，
所以如果是这个方案的话， 只能上2门功课。





"""


class Solution:
    def scheduleCourse(self, courses) -> int:
        # 过滤掉不合法的课程， 比如， 最后完成的日期比需要耗时的天数还要小
        this_courses = [course for course in courses if course[0] < course[1]]

        if len(this_courses) == 0:
            return 0
        elif len(this_courses) == 1:
            return 1
        else:
            for course in this_courses:
                pass


class Solution_chatgtp_v1:
    def scheduleCourse(self, courses) -> int:
        import heapq

        # 首先，将课程按照截止日期（lastDayi）进行排序
        courses.sort(key=lambda x: x[1])

        # 创建一个最大堆，用于存储课程的持续时间
        max_heap = []

        current_time = 0  # 当前时间，从第一天开始
        for duration, end_day in courses:
            # 尝试将当前课程加入课程表
            if current_time + duration <= end_day:
                heapq.heappush(max_heap, -duration)  # 以持续时间的相反数加入堆
                current_time += duration
            # 如果无法加入当前课程，则尝试用持续时间最长的课程替换掉已有的课程
            elif max_heap:
                longest_duration = -heapq.heappop(max_heap)  # 取出持续时间最长的课程
                if longest_duration > duration:
                    heapq.heappush(max_heap, -duration)  # 将当前课程加入堆
                    current_time += duration - longest_duration  # 调整当前时间
                else:
                    heapq.heappush(max_heap, -longest_duration)  # 将原持续时间最长的课程重新加入堆

        return len(max_heap)

