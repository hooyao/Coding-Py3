import sys
from typing import List


class Solution:
    def rotate_TLE(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) == 0:
            return
        remain = len(nums) - k
        end = len(nums) - 1
        while remain > k:
            for i in range(k):
                nums[end - i], nums[end - i - k] = nums[end - i - k], nums[end - i]
            remain = remain - k
        for i in reversed(range(remain)):
            pos = i
            target_pos = i + k
            while pos < target_pos:
                nums[pos], nums[pos + 1] = nums[pos + 1], nums[pos]
                pos += 1

    def rotate_cyclic(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % len(nums)
                nums[next], prev = prev, nums[next]
                current = next
                count += 1
                if start == current:
                    break
            start += 1


def main(*args):
    solution = Solution()
    nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
    solution.rotate_cyclic(nums, 3)
    print(nums)


if __name__ == '__main__':
    main(*sys.argv[1:])
