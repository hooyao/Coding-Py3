import math
import sys


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        number = int(math.fabs(x))
        pwr = int(math.log(number, 10))
        for r_idx in range(pwr + 1):
            tmp1 = self.get_digit(number, r_idx)
            tmp2 = self.get_digit(number, pwr - r_idx)
            if tmp1 != tmp2:
                return False
        return True

    def get_digit(self, number, r_pos):
        tmp1 = number % math.pow(10, r_pos + 1)
        return int(tmp1 / math.pow(10, r_pos))


def main(*args):
    num = 1000021
    num2 = 12321
    solution = Solution()

    result = solution.isPalindrome(0)
    print(solution.get_digit(10101, 3))
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
