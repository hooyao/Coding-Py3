import sys

from BTreeUtils import BTreeHelper
from BTreeUtils import TreeNode


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, value):
        """
        :type root: TreeNode
        :type value: int
        :rtype: bool
        """
        if not root:
            return False
        result = []
        self.recursive_add_path(root, result, 0)
        return value in result

    def recursive_add_path(self, root, result, up_sum):
        if not root:
            return
        if not root.left and not root.right:
            result.append(up_sum + root.val)
            return
        self.recursive_add_path(root.left, result, up_sum + root.val)
        self.recursive_add_path(root.right, result, up_sum + root.val)


def main(*args):
    tree_array = [1, 2]
    value = 22
    root = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(root)
    result = Solution().hasPathSum(root, value)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
