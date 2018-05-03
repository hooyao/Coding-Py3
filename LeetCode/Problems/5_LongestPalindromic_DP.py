import sys


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        result = ''
        d = [[0] * s_len for i in range(s_len)]
        for end in range(s_len):
            for start in range(end + 1):
                print(str(start) + ':' + str(end))
                if s[start] == s[end] and (end - start < 2 or d[start + 1][end - 1] == 1):
                    d[start][end] = 1
                if d[start][end] == 1 and end - start + 1 > len(result):
                    result = s[start:end + 1]
        return result


def main(*args):
    s = "babad"
    s1 = "cbbd"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
