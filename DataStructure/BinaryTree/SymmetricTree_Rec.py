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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.recursive_check_mirror(root.left, root.right)

    def recursive_check_mirror(self, left_root, right_root):
        if not left_root and not right_root:
            return True
        if left_root is None and right_root is not None or \
                left_root is not None and right_root is None:
            return False
        if not left_root.left and not left_root.right \
                and not right_root.left and not right_root.right \
                and left_root.val == right_root.val:
            return True
        if (left_root is None and right_root is not None) \
                or (left_root is not None and right_root is None) \
                or (left_root.val != right_root.val):
            return False
        return self.recursive_check_mirror(left_root.left, right_root.right) \
               and self.recursive_check_mirror(left_root.right, right_root.left)


def main(*args):
    tree_array = [4, -57, -57, None, 67, 67, None, None, -97, -97]
    root = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(root)
    result = Solution().isSymmetric(root)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
