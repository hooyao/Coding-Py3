import sys
from BTreeUtils import TreeNode
from BTreeUtils import BTreeHelper


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        self.recursive_preorder(root, result)
        return result

    def recursive_preorder(self, root, result):
        result.append(root.val)
        if root.left is not None:
            self.recursive_preorder(root.left, result)
        if root.right is not None:
            self.recursive_preorder(root.right, result)


def main(*args):
    tree_array = [5, 1, 2, 0, None, 3, 4, None, None, 6]
    root = BTreeHelper.list_to_tree(tree_array)
    result = Solution().preorderTraversal(root)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
