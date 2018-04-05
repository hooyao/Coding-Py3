import sys


class Solution:
    def isSubsetSum(self, a, x):
        """
        :type a: list
        :type x: int
        :rtype: bool
        """
        a.sort()
        dp = [[0] * (x + 1) for i in range(len(a))]
        for i in range(len(a)):
            dp[i][0] = 1

        for i in range(1, x + 1):
            if a[0] == i:
                dp[0][i] = 1

        for i in range(1, len(a)):
            for j in range(1, x + 1):
                if j < a[i - 1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-a[i-1]]
        print(dp)


def main(*args):
    values = [3, 34, 4, 12, 5, 2]
    x = 9
    result = Solution().isSubsetSum(values, x)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
