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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.recursive_build_from_inorder_postorder(inorder, postorder)

    def recursive_build_from_inorder_postorder(self, in_order, post_order):
        if len(in_order) != len(post_order):
            raise ValueError(
                'inorder len = {0} must be equal to postorder len= {1}'.format(len(in_order), len(post_order)))
        if len(in_order) == 0:
            return None
        root_val = post_order[-1]
        root_node = TreeNode(root_val)
        in_order_root_index = in_order.index(root_val)
        in_order_left_part = in_order[:in_order_root_index]
        in_order_right_part = in_order[in_order_root_index + 1:]

        post_order_left_end = 0
        if len(in_order_left_part) == 0:
            post_order_left_part = []
        else:
            # for idx in reversed(range(0, len(in_order) - 1)):
            #     if set(post_order[0:idx+1]) == set(in_order_left_part):
            #         post_order_left_end = idx
            #         break
            # post_order_left_part = post_order[0:post_order_left_end+1]
            post_order_left_part = post_order[0:len(in_order_left_part)]
        post_order_right_part_first_index = len(post_order_left_part)
        post_order_right_part = post_order[post_order_right_part_first_index:-1]

        left_root = self.recursive_build_from_inorder_postorder(in_order_left_part, post_order_left_part)
        righ_root = self.recursive_build_from_inorder_postorder(in_order_right_part, post_order_right_part)

        root_node.left = left_root
        root_node.right = righ_root
        return root_node


def main(*args):
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    #inorder = [1, 2, 3]
    #postorder = [3, 2, 1]
    #inorder = [2, 1]
    #postorder = [2, 1]
    result = Solution().buildTree(inorder, postorder)
    BTreeHelper.pretty_print(result)

    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
