#!/usr/bin/env python  
""" 
@author:huyao 
@license: Apache Licence 
@file: bubble_sort.py 
@time: 2019/03/27
@contact: huy@tradeshift.com
@site:  
@software: PyCharm 
"""
import random
import sys
from typing import List


class Solution:
    def bubble_sort(self, data: List) -> List:
        for i in range(0, len(data)):
            flag = False
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    flag = True
            if not flag:
                break
        return data


def main(*args):
    #Solution().bubble_sort([4, 5, 6, 3, 2, 9])
    for i in range(100):
        arr = list(random.randrange(2000) for i in range(500))
        result = Solution().bubble_sort(arr)
        sorted_arr = sorted(arr)
        if result != sorted_arr:
            print(arr)
            print(sorted_arr)
            print("error")
            break


if __name__ == '__main__':
    main(*sys.argv[1:])
