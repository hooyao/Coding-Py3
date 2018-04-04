import sys


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[-1]


def main(*args):
    cost = [0,0,0,1]
    solution = Solution()
    result = solution.minCostClimbingStairs(cost)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
