import sys


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s_nums = sorted(nums)
        min_diff = sys.maxsize
        result = set()
        for i in range(len(s_nums) - 2):
            for j in range(i + 1, len(s_nums) - 1):
                expected = target - s_nums[i] - s_nums[j]
                if s_nums[j + 1] - expected > min_diff:
                    continue
                val, diff = self.bsearch(s_nums[j + 1:], expected)
                if diff < min_diff:
                    min_diff = diff
                    result = (s_nums[i], s_nums[j], val)
        return sum(result)

    def bsearch(self, arr, n):
        left, right = 0, len(arr) - 1
        while right - left > 1:
            mid = (right + left) // 2
            if arr[mid] < n:
                left = mid
            else:
                right = mid
        if abs(arr[left] - n) < abs(arr[right] - n):
            return arr[left], abs(arr[left] - n)
        else:
            return arr[right], abs(arr[right] - n)


def main(*args):
    solution = Solution()
    result = solution.threeSumClosest([-1, 2, 1, -4], 1)
    print(result)
    # print(solution.bsearch(sorted([-1, 2, 1, -4]), 1))


if __name__ == '__main__':
    main(*sys.argv[1:])
