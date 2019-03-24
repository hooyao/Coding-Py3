#!/usr/bin/env python  
""" 
@author:shz 
@license: Apache Licence 
@file: ReverseString.py 
@time: 2019/03/24
@contact: sunhouzan@163.com
@site:  
@software: PyCharm

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
import sys
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0, len(s) - 1)
        return s

    def helper(self, s, l_idx, r_idx):
        if r_idx - l_idx > 0:
            s[l_idx], s[r_idx] = s[r_idx], s[l_idx]
            self.helper(s, l_idx + 1, r_idx - 1)


def main(*args):
    # input_data = ["h", "e", "l", "l", "o"]
    input_data = ["H",'A',"T","B"]
    output = Solution().reverseString(input_data)
    print(output)


if __name__ == '__main__':
    main(*sys.argv[1:])
