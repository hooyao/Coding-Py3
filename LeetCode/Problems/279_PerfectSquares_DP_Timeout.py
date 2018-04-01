import math
import sys
import time


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        start_time = time.time()
        d = [0] * (n + 1)
        max_n = int(math.sqrt(n))
        ss = list(map(lambda i: i * i, range(1, max_n + 1)))
        print("--- %s seconds ---" % (time.time() - start_time))
        for i in range(1, n + 1):
            max_j = int(math.sqrt(n))
            d[i] = i
            for j in range(0, max_j):
                di = d[i]
                if di != 1:
                    j1 = ss[j]
                    if i - j1 > 0:
                        if d[i - j1] + 1 < di:
                            d[i] = d[i - j1] + 1
                    elif i == j1:
                        d[i] = 1
                        continue
        return d[n]


def main(*args):
    solution = Solution()

    start_time = time.time()
    result = solution.numSquares(8558)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
