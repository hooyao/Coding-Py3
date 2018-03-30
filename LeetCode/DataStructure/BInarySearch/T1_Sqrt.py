import sys


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        if x <= 1:
            return x
        while right - left > 1:
            mid = (left + right) // 2
            midp2 = mid * mid
            if midp2 == x:
                return mid
            elif midp2 < x:
                left = mid
            else:
                right = mid
        return left


def main(*args):
    num = 4
    num1 = 9
    num2 = 8
    result = Solution().mySqrt(2)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
