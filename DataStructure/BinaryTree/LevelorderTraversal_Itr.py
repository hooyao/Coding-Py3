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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result
        level = [root]
        while len(level) > 0:
            level, tmp = self.get_level_kids(level)
            result.append(tmp)
        return result

    def get_level_kids(self, level):
        kids = []
        tmp = []
        for ele in level:
            if ele.left:
                kids.append(ele.left)
            if ele.right:
                kids.append(ele.right)
            tmp.append(ele.val)
        return kids, tmp


def main(*args):
    tree_array = [3, 9, 20, None, None, 15, 7]
    root = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(root)
    result = Solution().levelOrder(root)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
