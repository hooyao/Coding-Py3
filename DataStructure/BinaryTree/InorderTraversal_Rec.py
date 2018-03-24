import sys
from BTreeUtils import TreeNode
from BTreeUtils import BTreeHelper


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        self.recursive_inorder(root, result)
        return result

    def recursive_inorder(self, root, result):
        if root.left is not None:
            self.recursive_inorder(root.left, result)
        result.append(root.val)
        if root.right is not None:
            self.recursive_inorder(root.right, result)


def main(*args):
    tree_array = [5, 1, 2, 0, None, 3, 4, None, None, 6]
    root = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(root)
    result = Solution().inorderTraversal(root)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
