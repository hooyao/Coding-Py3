import sys


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        min = nums[0]
        min_idx = 0
        for idx, value in enumerate(nums):
            if nums[idx] < min:
                min = nums[idx]
                min_idx = idx

        sorted_nums = []
        sorted_nums.extend(nums[min_idx:])
        sorted_nums.extend(nums[0:min_idx])
        left = 0
        right = len(sorted_nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if target == sorted_nums[mid]:
                result = mid
                break
            elif target > sorted_nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if result >= 0:
            result = (result + min_idx) % len(sorted_nums)
        return result


def main(*args):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    nums1 = [-1, 0, 5]
    target1 = 5
    result = Solution().search(nums, target)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
