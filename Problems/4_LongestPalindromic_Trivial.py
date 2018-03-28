import sys


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_start = 0
        max_end = 0
        for i in range(len(s)):
            start_odd, end_odd = self.expand(s, i, i)
            odd_len = end_odd - start_odd + 1
            start_even, end_even = self.expand(s, i, i + 1)
            even_len = end_even - start_even + 1
            if odd_len > even_len:
                if odd_len > max_end - max_start + 1:
                    max_start = start_odd
                    max_end = end_odd
            else:
                if even_len > max_end - max_start + 1:
                    max_start = start_even
                    max_end = end_even
        return s[max_start:max_end + 1]

    def expand(self, s, st, ed):
        start = st
        end = ed
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return start + 1, end - 1


def main(*args):
    s = "babad"
    s1 = "cbbd"
    s2 = "ccc"
    solution = Solution()
    result = solution.longestPalindrome(s2)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
