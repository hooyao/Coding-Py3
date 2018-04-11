import sys


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for i in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not (i == 1 and j == 1):
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        return dp[-1][-1]


def main(*args):
    solution = Solution()
    result = solution.uniquePaths(3, 7)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
