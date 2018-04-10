import sys


class Solution(object):
    def LCS(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1_len = len(s1)
        s2_len = len(s2)
        dp = [[0] * s2_len for i in range(s1_len)]
        for i in range(0, s1_len):
            for j in range(0, s2_len):
                if s1[i] == s2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def LCS_ROLLING(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1_len = len(s1)
        s2_len = len(s2)
        last_dp = [0] * s2_len
        this_dp = [0] * s2_len
        for i in range(0, s1_len):
            for j in range(0, s2_len):
                if s1[i] == s2[j]:
                    if i == 0 or j == 0:
                        this_dp[j] = 1
                    else:
                        this_dp[j] = last_dp[j - 1] + 1
                else:
                    this_dp[j] = max(last_dp[j], this_dp[j - 1])
            last_dp = list(this_dp)
        return this_dp[-1]

def main(*args):
    a = 'ABCBDAB'
    b = 'BDCABA'
    solution = Solution()
    result = solution.LCS_ROLLING(a, b)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
