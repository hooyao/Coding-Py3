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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.recursive_bottom_up(root)

    def recursive_bottom_up(self, root):
        if root is None:
            return 0
        left_depth = self.recursive_bottom_up(root.left)
        right_depth = self.recursive_bottom_up(root.right)
        return max(left_depth, right_depth) + 1


def main(*args):
    tree_array = [3, 9, 20, None, None, 15, 7]
    root = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(root)
    result = Solution().maxDepth(root)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
