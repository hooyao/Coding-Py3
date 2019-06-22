#!/usr/bin/env python  
""" 
@author:huyao 
@license: Apache Licence 
@file: merge_sort_20190329.py 
@time: 2019/03/29
@contact: huy@tradeshift.com
@site:  
@software: PyCharm 
"""
import random
import sys
import time
from typing import List


class Solution:
    def merge_sort(self, unsorted_data):
        self.resursive_merge_sort(unsorted_data, 0, len(unsorted_data) - 1)

    def resursive_merge_sort(self, data, start, end):
        if start < end:
            middle = (end + start) // 2
            self.resursive_merge_sort(data, start, middle)
            self.resursive_merge_sort(data, middle + 1, end)
            merged = self.merge(data[start:middle + 1], data[middle + 1:end + 1])
            data[start:end + 1] = merged

    def merge(self, left_data: List, right_data: List) -> List:
        target = [0] * (len(left_data) + len(right_data))
        left_idx = 0
        right_idx = 0
        target_idx = 0
        while left_idx < len(left_data) and right_idx < len(right_data):
            if left_data[left_idx] > right_data[right_idx]:
                target[target_idx] = right_data[right_idx]
                right_idx = right_idx + 1
            else:
                target[target_idx] = left_data[left_idx]
                left_idx = left_idx + 1
            target_idx = target_idx + 1
        whatsleft_on_left = [] if left_idx >= len(left_data) else left_data[left_idx:]
        whatsleft_on_right = [] if right_idx >= len(right_data) else right_data[right_idx:]
        target[target_idx:target_idx + len(whatsleft_on_left)] = whatsleft_on_left
        target[target_idx + len(whatsleft_on_left):
               target_idx + len(whatsleft_on_left) + len(whatsleft_on_right)] \
            = whatsleft_on_right

        return target


def main(*args):
    solution = Solution()
    # print(result)
    # arr = random.sample(range(10), 10)

    # test merge correctness
    # for i in range(1000):
    #     left = list(sorted(random.randrange(100) for i in range(random.randrange(30, 50))))
    #     right = list(sorted(random.randrange(100) for i in range(random.randrange(30, 50))))
    #     merged = solution.merge(left, right)
    #     expected = sorted(left + right)
    #     if expected != merged:
    #         print(merged)
    #         print(expected)
    #         print("error!!")
    #         break

    # print(merged)
    t = time.process_time()
    for i in range(1000):
        arr = list(random.randrange(10000) for i in range(random.randrange(400, 600)))
        solution.merge_sort(arr)
        sorted_arr = sorted(arr)
        if arr != sorted_arr:
            print(arr)
            print(sorted_arr)
            print("error")
            break
    eclapsed = time.process_time() - t
    print(eclapsed)


if __name__ == '__main__':
    main(*sys.argv[1:])
