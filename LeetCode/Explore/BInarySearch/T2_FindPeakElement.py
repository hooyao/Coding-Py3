import sys


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        for idx, value in enumerate(nums):
            if idx == 0 and nums[idx] > nums[idx + 1]:
                return 0
            if idx == len(nums) - 1 and nums[idx] > nums[idx - 1]:
                return idx
            if nums[idx] > nums[idx - 1] and nums[idx] > nums[idx + 1]:
                return idx
        return -1
    
def main(*args):
    result = Solution().findPeakElement([1])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])