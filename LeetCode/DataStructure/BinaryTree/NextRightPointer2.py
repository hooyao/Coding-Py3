class TreeLinkNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or (not root.left and not root.right):
            return root
        level = dict()
        lv = 0
        level[lv] = [root]
        next_level = self.get_kids(level[lv])
        while len(next_level) > 0:
            for i in range(len(next_level) - 1):
                next_level[i].next = next_level[i + 1]
            lv += 1
            next_level = self.get_kids(next_level)
        return root

    def get_kids(self, last_level):
        result = []
        for ele in last_level:
            if ele.left:
                result.append(ele.left)
            if ele.right:
                result.append(ele.right)
        return result

