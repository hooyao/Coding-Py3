import sys
import math


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        length = int(math.log(abs(x), 10))
        tmp_num = x
        result = 0
        for i in range(length + 1):
            t1 = math.pow(10, length - i)
            tmp = int(tmp_num / t1)
            tmp_num = tmp_num - tmp * math.pow(10, length - i)
            result = result + tmp * math.pow(10, i)
        if int(result) > 2147483647 or int(result) < -2147483648:
            return 0
        else:
            return int(result)


def main(*args):
    num = 0
    solution = Solution()
    result = solution.reverse(num)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
