import sys

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
#
# Follow up:
# Could you solve it in linear time?
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        result = [0] * (len(nums) - k + 1)
        q = deque()
        for i in range(k):
            if len(q) == 0:
                q.append((nums[i], i))
            else:
                if nums[i] < q[-1][0]:
                    q.append((nums[i], i))
                else:
                    while len(q) > 0:
                        if q[-1][0] <= nums[i]:
                            q.pop()
                        else:
                            break
                    q.append((nums[i], i))
        result[0] = q[0][0]
        for i in range(k, len(nums)):
            window_start = i + 1 - k
            if len(q) == 0:
                q.append((nums[i], i))
            else:
                if nums[i] < q[-1][0]:
                    q.append((nums[i], i))
                else:
                    while len(q) > 0:
                        if q[-1][0] <= nums[i]:
                            q.pop()
                        else:
                            break
                    q.append((nums[i], i))
            while len(q) > 0:
                if q[0][1] < window_start:
                    q.popleft()
                else:
                    break
            result[window_start] = q[0][0]
        return result


def main(*args):
    solution = Solution()
    result = solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 1)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
