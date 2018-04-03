import sys


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #start from 0
        dp = [0]*(len(cost)+1)
        #start from 1

def main(*args):
    solution = Solution()
    result = solution.minCostClimbingStairs()
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])