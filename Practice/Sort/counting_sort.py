#!/usr/bin/env python  
""" 
@author:huyao 
@license: Apache Licence 
@file: counting_sort.py 
@time: 2019/04/01
@contact: huy@tradeshift.com
@site:  
@software: PyCharm 
"""
import random
import sys
import time
from collections import Counter
from typing import List


class Solution:
    def counting_sort(self, unsorted_data: List) -> List:
        result = []
        cnt = Counter()
        for ele in unsorted_data:
            cnt[ele] += 1
        for key in sorted(cnt):
            data = [key for i in range(cnt[key])]
            result = result + data
        return result

    def recursive_quick_sort(self, unsorted_data):
        self.partition(unsorted_data, 0, len(unsorted_data) - 1)
        return unsorted_data

    def partition(self, data, start, end):
        if end - start > 0:
            pivot = data[end]
            left = start
            right = end - 1
            while right - left >= 0:
                if data[left] >= pivot >= data[right]:
                    data[left], data[right] = data[right], data[left]
                    left += 1
                    right -= 1
                elif data[left] <= pivot:
                    left += 1
                elif data[right] >= pivot:
                    right -= 1
            data[end], data[right + 1] = data[right + 1], data[end]
            self.partition(data, start, right)
            self.partition(data, right + 2, end)


def main(*args):
    test_data1 = [random.randrange(0, 751) for i in range(1000*1000*5)]
    test_data2 = test_data1[:]
    start1 = time.process_time()
    expected = Solution().recursive_quick_sort(test_data1)
    end1 = time.process_time()
    print(end1 - start1)

    start2 = time.process_time()
    bucket_sorted = Solution().counting_sort(test_data2)
    end2 = time.process_time()
    print(end2 - start2)

    assert expected == bucket_sorted


if __name__ == '__main__':
    main(*sys.argv[1:])
