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
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        current_node = root
        parent_node = None
        position = 0
        while current_node:
            if key == current_node.val:
                break
            elif key < current_node.val:
                parent_node = current_node
                position = -1
                current_node = current_node.left
            else:
                parent_node = current_node
                position = 1
                current_node = current_node.right
        return self.del_node(parent_node, position,current_node)

    def del_node(self, parent_node, position, current_node):
        if current_node:
            if not current_node.left and not current_node.right:
                if parent_node:
                    self.assign_to_node(parent_node, position, None)
                else:
                    # remove root
                    return None
            if current_node.left and not current_node.right:
                if parent_node:
                    self.assign_to_node(parent_node, position, current_node.left)
                else:
                    return current_node.left
            if current_node.right and not current_node.left:
                if parent_node:
                    self.assign_to_node(parent_node, position, current_node.right)
                else:
                    return current_node.right
            if current_node.left and current_node.right:
                    tmp = current_node.right
                    tmp_parent = current_node
                    while tmp.left:
                        tmp_parent = tmp

                    cur_left = current_node.left
                    cur_right = current_node.right
                    target_node = tmp.left
                    tmp_right = target_node.right
                    tmp.left = current_node
                    current_node.left = None
                    current_node.right = tmp_right
                    target_node.left = cur_left
                    target_node.right = cur_right
                    if parent_node:
                        self.assign_to_node(parent_node, position, target_node)
                    else:
                        parent_node = target_node
                    tmp_parent = tmp

                    self.del_node(tmp_parent, -1, tmp_parent.left)
            return parent_node

    def assign_to_node(self, node, pos, another_node):
        if pos == -1:
            node.left = another_node
        if pos == 1:
            node.right = another_node


def main(*args):
    tree_array = [5,3,6,2,4,None,7]
    root = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(root)
    result = Solution().deleteNode(root, 3)
    BTreeHelper.pretty_print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
