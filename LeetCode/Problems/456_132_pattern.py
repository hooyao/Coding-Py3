import sys
from typing import List

#TODO TLE
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for ele in nums:
            if len(stack) == 0:
                stack.append((ele, ele))
            else:
                if ele < stack[-1][0]:
                    stack.append((ele, ele))
                    continue
                pos = len(stack) - 1
                while pos >= 0:
                    intv = stack[pos]
                    if intv[0] < ele < intv[1]:
                        return True
                    if pos > 0:
                        last_intv = stack[pos - 1]
                        if intv[1] < ele < last_intv[0]:
                            uppper = ele
                            lower = stack[-1][0]
                            stack = stack[0:pos]
                            stack.append((lower, uppper))
                            break
                    else:
                        if ele > intv[1]:
                            stack = [(stack[-1][0], ele)]
                            break
                    pos -= 1
        return False


def main(*args):
    solution = Solution()
    result = solution.find132pattern(
        [1, 3, -1, 8, -7, -3, 6])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
