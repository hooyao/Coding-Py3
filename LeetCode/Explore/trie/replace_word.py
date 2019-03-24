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

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self
        for idx, letter in enumerate(word):
            if letter not in current_node.kids:
                return False
            current_node = current_node.kids[letter]
            if idx == len(word) - 1 and current_node.isWord:
                return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self
        for idx, letter in enumerate(prefix):
            if letter not in current_node.kids:
                return False
            current_node = current_node.kids[letter]
        return True


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        word_list = sentence.split(" ")
        sorted_dict = sorted(dict, key=lambda x: len(x))
        result = ""
        for idx, ele in enumerate(word_list):
            result += self.transform_word(sorted_dict, ele)
            if idx < len(word_list) - 1:
                result += " "
        return result

    def transform_word(self, dict, word):
        trie = Trie()
        trie.insert(word)
        for root in dict:
            if trie.startsWith(root):
                return root
        return word


def main(*args):
    solution = Solution()
    dict = ["cat", "bat", "rat"]

    print(solution.replaceWords(dict, "the cattle was rattled by the battery"))


if __name__ == '__main__':
    main(*sys.argv[1:])
