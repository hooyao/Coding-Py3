import sys


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lenthOfLIS_bsearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        dp = [-sys.maxsize - 1, nums[0]]  # the smallest number if given LIS
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                idx = self.bsearch(dp, nums[i])
                dp[idx] = nums[i]
        return len(dp) - 1

    def bsearch(self, arr, val):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                right = mid
            else:
                left = mid

        return right


def main(*args):
    a = [4, 10, 4, 3, 8, 9]
    b = [10, 9, 2, 5, 3, 7, 101, 18]
    solution = Solution()
    c = [1]
    result = solution.lenthOfLIS_bsearch(a)
    # result = solution.bsearch(c, 2)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
