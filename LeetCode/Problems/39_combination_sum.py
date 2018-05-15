import sys


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.dfs(candidates, target)

    def dfs(self, candidates, target):
        result = []
        for i in range(len(candidates)):
            new_target = target - candidates[i]
            if new_target == 0:
                result.append([candidates[i]])
            elif new_target > 0:
                tmp = self.dfs(candidates[i:], new_target)
                for ele in tmp:
                    ele.insert(0, candidates[i])
                result += tmp
        return result


def main(*args):
    solution = Solution()
    result = solution.combinationSum([3, 2, 5], 8)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
