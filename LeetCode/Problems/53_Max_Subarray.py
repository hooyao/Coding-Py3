import sys


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # largest = nums[0]
        # dp = [[0]*len(nums) for i in range(len(nums))]
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if j > i:
        #             dp[i][j] = dp[i][j-1] + nums[j]
        #         else:
        #             dp[i][j] = nums[j]
        #         if dp[i][j] > largest:
        #             largest = dp[i][j]
        # return largest

        largest = nums[0]
        current_sum = largest
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            largest = max(largest, current_sum)
        return largest


def main(*args):
    solution = Solution()
    result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
