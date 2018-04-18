import sys


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
    def toBS(self, num):
        tmp = num
        result = ""
        while tmp > 0:
            result += str(tmp % 2)
            tmp = tmp // 2
        return result[::-1]


def main(*args):
    solution = Solution()
    # result = solution.findMaximumXOR([3, 10, 5, 25, 2, 8])
    result = solution.toBS(4)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
