import sys
import time


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        sorted_nums = sorted(nums)

        start_time = time.time()
        result = self.sum_rec(sorted_nums, target, 4)
        # result = self.sum_rec_set(set(nums), target, 4)
        end_time = time.time()
        print(str(end_time - start_time))
        return list(result)

    def sum_rec(self, nums, target, n):
        if len(nums) < n or target < nums[0] * n or target > nums[-1] * n:
            return []
        elif n == 2:
            return self.two_sum_set(nums, target)
        else:
            this_rec_result = []
            i = 0
            while i < len(nums):
                val = nums[i]
                new_target = target - val
                new_nums = nums[i + 1:]
                rec_result = self.sum_rec(new_nums, new_target, n - 1)
                for ele in rec_result:
                    this_rec_result.append([val] + ele)
                while i < len(nums) and nums[i] == val:
                    i += 1
            return this_rec_result

    def two_Sum(self, nums, target):
        if len(nums) > 0:
            this_rec_result = []
            i, j = 0, len(nums) - 1
            while i < j:
                cur_i_val = nums[i]
                cur_j_val = nums[j]
                if cur_i_val + cur_j_val == target:
                    this_rec_result.append([cur_i_val, cur_j_val])
                    while nums[i] == cur_i_val and i < j:
                        i += 1
                    while nums[j] == cur_j_val and i < j:
                        j -= 1
                elif cur_i_val + cur_j_val > target:
                    while nums[j] == cur_j_val and i < j:
                        j -= 1
                else:
                    while nums[i] == cur_i_val and i < j:
                        i += 1
            return this_rec_result
        else:
            return []

    def two_sum_set(self, nums, target):
        d = set()
        result = set()
        for ele in nums:
            if target - ele in d:
                result.add((target - ele, ele))
            d.add(ele)
        return [list(item) for item in result]


def main(*args):
    solution = Solution()
    result = solution.two_sum_set([0, 0, 0, 0], 0)
    # result = solution.fourSum(
    #     [1, 0, -1, 0, -2, 2],
    #     0
    # )

    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
