import sys


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_val = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            if nums[i] < last_val:
                val, relative_pos = self.bsearch(nums[i + 1:], nums[i])
                tmp = nums[i]
                nums[i] = nums[i + 1 + relative_pos]
                nums[i + 1 + relative_pos] = tmp
                nums[i + 1:] = reversed(nums[i + 1:])
                return
            last_val = nums[i]
        nums.reverse()

    def bsearch(self, arr, target):
        if target < arr[-1]:
            return arr[-1], len(arr) - 1
        if len(arr) <= 2:
            for i in reversed(range(len(arr))):
                if arr[i] > target:
                    return arr[i], i
        left, right = 0, len(arr) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if arr[mid] > target:
                left = mid
            else:
                right = mid

        return arr[left], left


def main(*args):
    solution = Solution()
    p1 = [1, 2, 3]
    p2 = [3, 2, 1]
    p3 = [1, 1, 5]
    p4 = [2, 2, 0, 4, 3, 1]

    p5 = [6, 5, 3, 1]
    solution.nextPermutation(p4)
    print(p4)


# result = solution.bsearch([4, 3, 1], 0)
# print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
