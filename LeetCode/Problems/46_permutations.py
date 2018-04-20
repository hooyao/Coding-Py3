import sys


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_set = set(nums)
        return self.permute_rec(nums_set)

    def permute_rec(self, nums_set):
        if len(nums_set) == 1:
            return [list(nums_set)]
        result = []
        for idx, val in enumerate(nums_set):
            new_set = set(nums_set)
            new_set.remove(val)
            perms = self.permute(new_set)
            for ele in perms:
                result.append([val] + ele)
        return result

    def permute_iter(self, nums):
        nums = sorted(nums)
        result = []
        result.append([nums[0]])
        for idx in range(1, len(nums)):
            ele = nums[idx]
            new_perm = []
            for perm in result:
                for i in range(len(perm)+1):
                    new_perm.append(perm[:i] + [ele] + perm[i:])
            result = new_perm
        return result


def main(*args):
    solution = Solution()
    result = solution.permute_iter([1, 2, 3])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
