class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isKey = False
        self.val = 0
        self.kids = dict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        current_node = self
        for idx, letter in enumerate(key):
            if letter not in current_node.kids:
                current_node.kids[letter] = MapSum()
            current_node = current_node.kids[letter]
            if idx == len(key) - 1:
                current_node.val = val
                current_node.isKey = True

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        current_node = self
        result = 0
        all_kids = None
        for idx, letter in enumerate(prefix):
            if letter not in current_node.kids:
                return 0
            current_node = current_node.kids[letter]
            if idx == len(prefix) - 1:
                if current_node.isKey:
                    result += current_node.val
                all_kids = current_node.kids
        to_do = list(all_kids.values())
        while len(to_do) > 0:
            new_todo = []
            for ele in to_do:
                if ele.isKey:
                    result += ele.val
                new_todo += list(ele.kids.values())
            to_do = new_todo

        return result

    # Your MapSum object will be instantiated and called as such:


obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("apple"))
obj.insert("app", 2)
print(obj.sum("ap"))
# param_2 = obj.sum(prefix)
