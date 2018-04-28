import sys


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            raise Exception()
        left, right = 0, len(height) - 1
        max_c = 0

        while right - left > 0:
            c = min(height[left], height[right]) * (right - left)
            max_c = max(c, max_c)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_c


def main(*args):
    solution = Solution()
    result = solution.maxArea([1, 3, 2, 5, 25, 24, 5])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
