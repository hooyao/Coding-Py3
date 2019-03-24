import sys


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.kids = dict()
        self.isWord = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current_node = self
        for idx, letter in enumerate(word):
            if letter not in current_node.kids:
                current_node.kids[letter] = Trie()
                current_node.kids[letter].val = letter
            current_node = current_node.kids[letter]
            if idx == len(word) - 1:
                current_node.isWord = True


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_b = []
        for ele in nums:
            nums_b.append(self.toBS(ele))
        trie_root = Trie()
        for ele in nums_b:
            trie_root.insert(ele)

        max_result = 0
        for num in nums_b:
            cur_trie = trie_root
            result = ""
            for idx in range(len(num)):
                digit = num[idx]
                kids = cur_trie.kids
                tmp = self.xor(digit, "1")
                if tmp in kids:
                    result += "1"
                    cur_trie = cur_trie.kids[tmp]
                else:
                    result += "0"
                    cur_trie = cur_trie.kids[self.xor(digit, "0")]
            if len(result) == len(num):
                if int(result, 2) > max_result:
                    max_result = int(result, 2)
        return max_result

    def toBS(self, num):
        tmp = num
        result = ""
        while tmp > 0:
            result += str(tmp % 2)
            tmp = tmp // 2
        padding = ""
        for i in range(len(result), 32):
            padding += "0"
        result += padding
        return result[::-1]

    def xor(self, a, b):
        if a == b:
            return "0"
        else:
            return "1"

    def flip(self, a):
        if a == "0":
            return "1"
        else:
            return "0"


def main(*args):
    solution = Solution()
    result = solution.findMaximumXOR([89,102,183,233,175,87,497,350,348,191,136,497,166,420,279,212,269,125,262,74])
    # result = solution.toBS(4)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
