import sys


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, idx_r = 0, 0
        last_val = None
        while idx < len(nums):
            if last_val is None:
                last_val = nums[idx]
                idx += 1
                idx_r += 1
                continue
            if nums[idx] == last_val:
                idx += 1
                continue
            else:
                last_val = nums[idx]
                nums[idx_r] = nums[idx]
                idx += 1
                idx_r += 1
        return idx_r


def main(*args):
    solution = Solution()
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = solution.removeDuplicates(arr)
    print(arr)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
