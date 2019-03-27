#!/usr/bin/env python  
""" 
@author:huyao 
@license: Apache Licence 
@file: insert_sort.py 
@time: 2019/03/27
@contact: huy@tradeshift.com
@site:  
@software: PyCharm 
"""
import random
import sys
from typing import List


class Solution:
    def insert_sort(self, data: List) -> List:
        for idx in range(1, len(data)):
            key = data[idx]
            i = idx - 1
            while i >= 0 and key < data[i]:
                data[i + 1] = data[i]
                i = i - 1
            data[i + 1] = key
        return data


def main(*args):
   # print(Solution().insert_sort(list(random.randrange(10) for i in range(30))))

    for i in range(100):
        arr = list(random.randrange(2000) for i in range(1234))
        result = Solution().insert_sort(arr)
        sorted_arr = sorted(arr)
        if result != sorted_arr:
            print(arr)
            print(sorted_arr)
            print("error")
            break


if __name__ == '__main__':
    main(*sys.argv[1:])
