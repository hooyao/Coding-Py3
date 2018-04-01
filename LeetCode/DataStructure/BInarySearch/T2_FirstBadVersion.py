import sys


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def isBadVersion(self, version):
        return version >=9


def main(*args):
    result = Solution().firstBadVersion(9)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
