import sys


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_count = len(nums)
        m = 1 << num_count
        result = []
        for i in range(m):
            tmp = i
            tmp_result = []
            for j in range(num_count):
                if tmp & (1 << j) != 0:
                    tmp_result.append(nums[j])
            result.append(tmp_result)
        return result


def main(*args):
    solution = Solution()
    result = solution.subsets([1, 2, 3])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
