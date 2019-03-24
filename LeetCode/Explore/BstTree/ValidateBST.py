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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        return self.recursive_check(root, None, None)

    def recursive_check(self, root, mi, ma):
        if root and (not root.left and not root.right):
            return self.is_larger(root.val, mi) and self.is_smaller(root.val, ma)
        is_left = True
        if root.left:
            is_left = self.recursive_check(root.left, mi, root.val) \
                      and self.is_larger(root.left.val, mi) \
                      and self.is_smaller(root.left.val, root.val)
        is_right = True
        if root.right:
            is_right = self.recursive_check(root.right, root.val, ma) \
                       and self.is_smaller(root.val, root.right.val) \
                       and self.is_smaller(root.right.val, ma)
        return is_left and is_right

    def is_larger(self, a, b):
        if b is None:
            return True
        else:
            return a > b

    def is_smaller(self, a, b):
        if b is None:
            return True
        else:
            return a < b


def main(*args):
    tree_array = [0, 1]
    root = BTreeHelper.list_to_tree(tree_array)
    result = Solution().isValidBST(root)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
