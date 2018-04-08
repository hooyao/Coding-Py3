import sys


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rm = dict()
        rm['I'] = 1
        rm['V'] = 5
        rm['X'] = 10
        rm['L'] = 50
        rm['C'] = 100
        rm['D'] = 500
        rm['M'] = 1000
        arr = [0] * len(s)
        result = 0
        for idx, ele in enumerate(s):
            arr[idx] = rm.get(ele)


def main(*args):
    # Rule is too complicated
    solution = Solution()
    result = solution.romanToInt('MCMXCVI')
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
