#!/usr/bin/env python  
""" 
@author:huyao 
@license: Apache Licence 
@file: 238_Product_of_Array_Except_Self.py 
@time: 2019/06/14
@contact: huy@tradeshift.com
@site:  
@software: PyCharm 
"""
import sys
from typing import List

"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

"""


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1 for _i in range(len(nums))]
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        right_product = 1
        for i in reversed(range(len(nums))):
            tmp = left_product[i] * right_product
            right_product = nums[i] * right_product
            left_product[i] = tmp

        return left_product


def main(*args):
    solution = Solution()

    input = [1, 2, 3, 4, 5]
    print(solution.productExceptSelf(input))

    input = [1, 2, 0, 4, 5]
    print(solution.productExceptSelf(input))

    input = [0, 2, 3, 4, 5]
    print(solution.productExceptSelf(input))


if __name__ == '__main__':
    main(*sys.argv[1:])
