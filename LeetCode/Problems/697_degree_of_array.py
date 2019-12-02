import heapq
import sys
from typing import List, Dict


# Given a non-empty array of non-negative integers nums, the degree of this array is
# defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums,
# that has the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6


class Stat:
    def __init__(self, value: int, freq: int, start: int, end: int) -> None:
        self.value = value
        self.freq = freq
        self.start = start
        self.end = end

    def __lt__(self, other) -> bool:
        if self.freq != other.freq:
            return self.freq - other.freq < 0
        else:
            return (self.end - self.start) - (other.end - other.start) > 0


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq_dict: Dict[int, Stat]
        freq_dict = dict()
        for pos, value in enumerate(nums):
            if value in freq_dict:
                stat = freq_dict.get(value)
                stat.freq += 1
                stat.end = pos
            else:
                freq_dict[value] = Stat(value, 1, pos, pos)
        stat_list = list(freq_dict.values())
        heapq._heapify_max(stat_list)
        result = stat_list[0]
        return result.end - result.start + 1


def main(*args):
    solution = Solution()
    result = solution.findShortestSubArray([1])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
