import sys


class Solution:

    def __init__(self):
        self.kids = dict()
        self.val = None
        self.isWord = False

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) == 0:
            return result
        idx = 0
        while True:
            current_letter = ""
            for which, word in enumerate(strs):
                if len(word) <= idx:
                    return result
                else:
                    if which == 0:
                        current_letter = word[idx]
                    else:
                        if word[idx] != current_letter:
                            return result
            idx += 1
            result += current_letter


def main(*args):
    solution = Solution()
    result = solution.longestCommonPrefix([])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
