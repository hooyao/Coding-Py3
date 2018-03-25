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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.recursive_build_from_inorder_postorder(preorder, inorder)

    def recursive_build_from_inorder_postorder(self, pre_order, in_order):
        if len(in_order) != len(pre_order):
            raise ValueError(
                'inorder len = {0} must be equal to preorder len= {1}'.format(len(in_order), len(pre_order)))
        if len(in_order) == 0:
            return None
        root_val = pre_order[0]
        root_node = TreeNode(root_val)
        in_order_root_index = in_order.index(root_val)
        in_order_left_part = in_order[:in_order_root_index]
        in_order_right_part = in_order[in_order_root_index + 1:]

        pre_order_left_end = 0
        if len(in_order_left_part) == 0:
            pre_order_left_part = []
        else:
            # for idx in reversed(range(1, len(in_order))):
            #     if set(pre_order[1:idx + 1]) == set(in_order_left_part):
            #         pre_order_left_end = idx
            #         break
            # pre_order_left_part = pre_order[1:pre_order_left_end + 1]
            pre_order_left_part = pre_order[1:len(in_order_left_part) + 1]
        pre_order_right_part_first_index = len(pre_order_left_part) + 1
        pre_order_right_part = pre_order[pre_order_right_part_first_index:]

        left_root = self.recursive_build_from_inorder_postorder(pre_order_left_part, in_order_left_part)
        righ_root = self.recursive_build_from_inorder_postorder(pre_order_right_part, in_order_right_part)

        root_node.left = left_root
        root_node.right = righ_root
        return root_node


def main(*args):
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = Solution().buildTree(preorder, inorder)
    BTreeHelper.pretty_print(result)

    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
