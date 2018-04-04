import sys


class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [[] for i in range(target + 1)]
        for i in range(1, len(dp)):
            print(i)
            if i ==150:
                print('here')
            if i in nums:
                dp[i].append([i])
            for j in range(1, i):
                tmp_list = self.combine(dp[j], dp[i - j])
                for ele in tmp_list:
                    if ele not in dp[i]:
                        dp[i].append(ele)
        return len(dp[-1])

    def combine(self, c1, c2):
        result = []
        for i in range(len(c1)):
            for j in range(len(c2)):
                tmp = c1[i] + c2[j]
                result.append(tmp)
        return result


def main(*args):
    nums = [1, 2, 3]
    target = 4
    solution = Solution()
    result = solution.combinationSum4(nums, target)
    c1 = [[1, 1], [2]]
    c2 = [[1, 1], [2]]
    # result = solution.combine(c1, c2)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
