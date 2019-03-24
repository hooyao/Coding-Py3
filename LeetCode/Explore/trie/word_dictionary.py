class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kids = dict()
        self.val = None
        self.isWord = False

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current_node = self
        for idx, letter in enumerate(word):
            if letter not in current_node.kids:
                current_node.kids[letter] = WordDictionary()
                current_node.kids[letter].val = letter
            current_node = current_node.kids[letter]
            if idx == len(word) - 1:
                current_node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structur.e. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        todo = [self]
        for idx, letter in enumerate(word):
            if len(todo) == 0:
                break
            new_todo = []
            if letter == '.':
                for node in todo:
                    new_todo += list(node.kids.values())
            else:
                for node in todo:
                    if letter in node.kids:
                        new_todo.append(node.kids[letter])
                        if idx == len(word) - 1 and node.kids[letter].isWord:
                            return True
            todo = new_todo
        if len(todo) > 0 and word[-1] == '.':
            for ele in todo:
                if ele.isWord:
                    return True

        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
print(obj.addWord("at"))
print(obj.addWord("and"))
print(obj.addWord("an"))
print(obj.addWord("add"))
print(obj.search("a"))
print(obj.search(".at"))
print(obj.addWord("bat"))
print(obj.search(".at"))
print(obj.search("an."))
print(obj.search("a.d."))
print(obj.search("b."))
print(obj.search("a.d"))
print(obj.search("."))
