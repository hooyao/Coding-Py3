import sys


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        start = -1
        end = -1
        while left <= right:
            mid = (left + right) // 2
            mid_value = nums[mid]
            if mid_value == target and (mid == 0 or mid_value > nums[mid - 1]):
                start = mid
                break
            if mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        if start == -1:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = nums[mid]
            if mid_value == target and (mid == len(nums) - 1 or mid_value < nums[mid + 1]):
                end = mid
                break
            if mid_value > target:
                right = mid - 1
            else:
                left = mid + 1
        return [start, end]


def main(*args):
    result = Solution().searchRange([1, 2, 3, 4, 5], 1)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
