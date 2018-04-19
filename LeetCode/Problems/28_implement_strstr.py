import sys


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nl_len = len(needle)
        for i in range(len(haystack) - nl_len + 1):
            match = True
            for j in range(nl_len):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1


def main(*args):
    solution = Solution()
    result = solution.strStr("hello", "ld")
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
