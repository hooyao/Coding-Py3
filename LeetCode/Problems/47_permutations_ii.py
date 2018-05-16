import sys


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = set()
        for ele in nums:
            if len(result) == 0:
                result = {(ele,)}
            else:
                new_perm = set()
                for perm in result:
                    idx = 0
                    while idx < len(perm) + 1:
                        while idx < len(perm) and perm[idx] == ele:
                            idx += 1
                        new_perm.add(perm[:idx] + (ele,) + perm[idx:])
                        idx += 1

                result = new_perm
        return list(result)


def main(*args):
    solution = Solution()
    result = solution.permuteUnique([1, 1, 2, 2])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
