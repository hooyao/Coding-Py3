import sys


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def __init__(self):
        self.result = []

    def preorder(self, root):
        """
        :type
        root: Node
        :rtype: List[int]
        """
        return self.recursive_preorder(root)

    def recursive_preorder(self, root):
        self.result.append(root)
        if root.children and len(root.children) > 0:
            for kid in root.children:
                if kid:
                    self.preorder(kid)
