import sys


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


def main(*args):
    solution = Solution()
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
