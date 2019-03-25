#!/usr/bin/env python  
""" 
@author:hooyao
@license: Apache Licence 
@file: PascalTriangle.py 
@time: 2019/03/25
@contact:  hooyao@gmail.com
@site:  
@software: PyCharm

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
import sys
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows > 1:
            tmp = self.generate(numRows - 1)
            row = [1]
            for i in range(1, numRows - 1):
                row.append(tmp[-1][i - 1] + tmp[-1][i])
            row.append(1)
            tmp.append(row)
            return tmp


def main(*args):
    result = Solution().generate(5)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
