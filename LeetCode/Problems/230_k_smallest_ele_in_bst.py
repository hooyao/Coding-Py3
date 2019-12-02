import sys

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,None,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,None,None,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
from LeetCode.DataStructure.BstTree.BTreeUtils import BTreeHelper, TreeNode


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.visit_order = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inorder(root, k)

    def inorder(self, root, target):
        if root is None:
            return None
        result = self.inorder(root.left, target)
        if result is not None:
            return result
        self.visit_order += 1
        if self.visit_order == target:
            return root.val
        result = self.inorder(root.right, target)
        if result is not None:
            return result


def main(*args):
    tree_array = [31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9]
    root = BTreeHelper.list_to_tree(tree_array)
    k = 1
    solution = Solution()
    result = solution.kthSmallest(root, k)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
