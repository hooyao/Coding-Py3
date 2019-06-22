#!/usr/bin/env python  
""" 
@author:huyao 
@license: Apache Licence 
@file: bsearch.py 
@time: 2019/04/02
@contact: huy@tradeshift.com
@site:  
@software: PyCharm 
"""
import random
import sys
import time
from typing import List


class Solution:
    def bsearch(self, sorted_data: List, target: int) -> int:
        left = 0
        right = len(sorted_data) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = sorted_data[mid]
            if mid_val < target:
                left = mid + 1
            elif mid_val > target:
                right = mid - 1
            else:
                return mid
        return -1

    def bsearch_first_encounter(self, sorted_data: List, target: int) -> int:
        left = 0
        right = len(sorted_data) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = sorted_data[mid]
            if mid_val < target:
                left = mid + 1
            elif mid_val > target:
                right = mid - 1
            else:
                if mid == 0 or sorted_data[mid - 1] != mid_val:
                    return mid
                else:
                    right = mid - 1
        return -1


def main(*args):
    # test_data1 = list(sorted({random.randint(0, 1000 * 1000 * 2) for _ in range(1000 * 1000)}))
    # for _ in range(1000):
    #     target_idx = random.randint(0, len(test_data1))
    #     target1 = test_data1[target_idx]
    #     start1 = time.process_time()
    #     bs_idx_1 = Solution().bsearch(test_data1, target1)
    #     end1 = time.process_time()
    #     if bs_idx_1 != target_idx:
    #         print(f'{bs_idx_1}!={target_idx}')

    #Solution().bsearch_first_encounter([1,2,3,3,3,4,4,5,5,6,6,6,7,8],6)
    repeatable_test_data1 = list(sorted(random.randint(0, 1000 * 1000 * 2) for _ in range(1000 * 1000)))
    for _ in range(1000):
        target_idx = random.randint(0, len(repeatable_test_data1))
        target1 = repeatable_test_data1[target_idx]
        while target_idx > 0 and target1 == repeatable_test_data1[target_idx - 1]:
            target_idx -= 1
        start1 = time.process_time()
        bs_idx_1 = Solution().bsearch_first_encounter(repeatable_test_data1, target1)
        end1 = time.process_time()
        if bs_idx_1 != target_idx:
            print(f'{bs_idx_1}!={target_idx}')


if __name__ == '__main__':
    main(*sys.argv[1:])
