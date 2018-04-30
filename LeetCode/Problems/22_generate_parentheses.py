import sys


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.gen("", n)

    def gen(self, s, n):
        stack = []
        left_count = 0
        right_count = 0
        for letter in s:
            if len(stack) > 0 and stack[-1] == "(" and letter == ")":
                stack.pop()
            else:
                stack.append(letter)
            if letter == "(":
                left_count += 1
            else:
                right_count += 1
        result = []
        left_left = n - left_count
        right_left = n - right_count
        if left_left > 0:
            if len(stack) == 0:
                new_s = s + "("
                result += self.gen(new_s, n)
            else:
                new_s = s + "("
                result += self.gen(new_s, n)
                new_s = s + ")"
                result += self.gen(new_s, n)
        elif right_left > 0:
            tmp = ")" * right_left
            return [s + tmp]
        return result


def main(*args):
    solution = Solution()
    result = solution.generateParenthesis(8)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
