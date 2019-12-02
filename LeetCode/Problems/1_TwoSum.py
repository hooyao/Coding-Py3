import sys
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, n in enumerate(nums):
            j = d.get(target - n)
            if j is not None:
                return [j, i]
            d[n] = i
        return []


def main(*args):
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
