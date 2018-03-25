import sys


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        litter_bag = dict()
        largest_string = ''
        win_start = 0
        win_end = 0
        while win_end < n:
            if s[win_end] in litter_bag:
                win_start = max(litter_bag[s[win_end]]+1, win_start)
            litter_bag[s[win_end]] = win_end

            if win_end - win_start + 1 > len(largest_string):
                largest_string = s[win_start:win_end + 1]
            win_end += 1

        print(largest_string)
        return len(largest_string)


def main(*args):
    s = "abcabcbb"
    s1 = 'dvdf'
    s2 = "tmmzuxt"
    s4 = 'abcdefc'
    s5 = 'abccdefg'
    solution = Solution()
    # print(solution.test_repeat('abcdefg'))
    result = solution.lengthOfLongestSubstring(s5)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
