import sys


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1
        length = end - start + 1
        while length > 0:
            length = end - start + 1
            if length <= 2:
                for idx in range(start, end + 1):
                    if nums[idx] == target:
                        return idx
                return -1
            mid = int((start + end) / 2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid
            else:
                end = mid


def main(*args):
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    nums1 = [-1, 0, 5]
    target1 = 5
    result = Solution().search(nums1, target1)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
