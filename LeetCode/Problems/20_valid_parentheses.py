import sys


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ele in s:
            if len(stack) > 0:
                if self.isClose(stack[-1], ele):
                    stack.pop(-1)
                else:
                    stack.append(ele)
            else:
                stack.append(ele)
        return len(stack) == 0

    def isClose(self, a, b):
        if a == '[' and b == ']':
            return True
        if a == '{' and b == '}':
            return True
        if a == '(' and b == ')':
            return True
        return False


def main(*args):
    solution = Solution()
    result = solution.isValid("([)]")
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
