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
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current_node = root
        while current_node:
            if current_node.val > val:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = TreeNode(val)
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = TreeNode(val)
                    break
        return root


def main(*args):
    tree_array = [1, 0]
    root = BTreeHelper.list_to_tree(tree_array)
    val = 1
    result = Solution().insertIntoBST(root, 2)
    BTreeHelper.pretty_print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
