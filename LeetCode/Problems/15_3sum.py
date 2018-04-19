import sys


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        sorted_nums = sorted(nums)
        resultSet = set()
        last_val = 999
        for idx, val in enumerate(sorted_nums):
            if last_val == val:
                continue
            if val > 0:
                break
            i = idx + 1
            j = len(sorted_nums) - 1
            while i < j:
                cur_i_val = sorted_nums[i]
                cur_j_val = sorted_nums[j]
                if val + cur_i_val + cur_j_val == 0:
                    # resultSet.add((val, cur_i_val, cur_j_val))
                    result.append([val, cur_i_val, cur_j_val])
                    while sorted_nums[i] == cur_i_val and i < j:
                        i += 1
                    while sorted_nums[j] == cur_j_val and i < j:
                        j -= 1
                elif val + cur_i_val + cur_j_val > 0:
                    while sorted_nums[j] == cur_j_val and i < j:
                        j -= 1
                else:
                    while sorted_nums[i] == cur_i_val and i < j:
                        i += 1
            last_val = val
        # return [list(i) for i in resultSet]
        return result


def main(*args):
    solution = Solution()
    result = solution.threeSum([0,0,0])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
