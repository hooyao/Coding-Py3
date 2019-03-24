import sys

from BTreeUtils import BTreeHelper
from BTreeUtils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.recursive_top_down(root, 1)
        return self.depth

    def recursive_top_down(self, root, current_depth):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.depth = max(self.depth, current_depth)
        self.recursive_top_down(root.left, current_depth + 1)
        self.recursive_top_down(root.right, current_depth + 1)


def main(*args):
    tree_array = [1, 2, 3, 4, None, None, 5]
    root = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(root)
    result = Solution().maxDepth(root)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
