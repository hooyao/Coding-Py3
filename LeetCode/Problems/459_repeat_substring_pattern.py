import sys


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        for i in range(1, (len(s) + 1) // 2 + 1):
            if len(s) % i == 0 and self.checkPattern(s, i):
                return True
        return False

    def checkPattern(self, s, l):
        pattern = s[0:l]
        for j in range(1, len(s) // l):
            if s[j * l:(j + 1) * l] != pattern:
                return False
        return True


def main(*args):
    solution = Solution()
    result = solution.repeatedSubstringPattern("ab")
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
