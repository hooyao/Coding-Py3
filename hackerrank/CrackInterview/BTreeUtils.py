from collections import namedtuple
from io import StringIO
import math


# define the node structure
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.data = x
        self.left = left
        self.right = right

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.next = None

class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, b):
        self.queue.insert(0, b)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []


def getheight(node):
    if not node:
        return 0
    else:
        return max(getheight(node.left), getheight(node.right)) + 1


def add_padding(str, pad_length_value):
    str = str.strip()
    return str.center(pad_length_value, ' ')


class BTreeHelper:

    @staticmethod
    def list_to_tree(input_values):
        if input_values is None or len(input_values) is 0:
            return None
        root = TreeNode(int(input_values[0]))
        node_queue = [root]
        front = 0
        index = 1
        while index < len(input_values):
            node = node_queue[front]
            front = front + 1

            item = input_values[index]
            index = index + 1
            if item is not None:
                left_number = int(item)
                node.left = TreeNode(left_number)
                node_queue.append(node.left)

            if index >= len(input_values):
                break

            item = input_values[index]
            index = index + 1
            if item is not None:
                right_number = int(item)
                node.right = TreeNode(right_number)
                node_queue.append(node.right)
        return root

    @staticmethod
    def list_to_tree2(input):
        root = TreeNode(input[0])
        return BTreeHelper.insert_level_order(input, root, 1)

    @staticmethod
    def insert_level_order(input, root, idx_start):
        if idx_start < len(input):
            if input[idx_start] is not None:
                tmp = TreeNode(input[idx_start])
                root.left = BTreeHelper.insert_level_order(input, tmp, idx_start * 2 + 1)

            if input[idx_start + 1] is not None:
                tmp = TreeNode(input[idx_start + 1])
                root.right = BTreeHelper.insert_level_order(input, tmp, (idx_start + 1) * 2 + 1)
        return root

    @staticmethod
    def pretty_print(root):
        output = StringIO()
        pretty_output = StringIO()

        current_level = Queue()
        next_level = Queue()
        current_level.enqueue(root)
        depth = 0

        # get the depth of current tree
        # get the tree node data and store in list
        if root:
            while not current_level.isEmpty():
                current_node = current_level.dequeue()
                output.write('%s ' % current_node.data if current_node else 'N ')
                next_level.enqueue(
                    current_node.left if current_node else current_node)
                next_level.enqueue(
                    current_node.right if current_node else current_node)

                if current_level.isEmpty():
                    if sum([i is not None for i in next_level.queue]
                           ):  # if next level has node
                        current_level, next_level = next_level, current_level
                        depth = depth + 1
                    output.write('\n')
        # print('the tree printed level by level is :')
        # print(output.getvalue())
        # print("current tree's depth is %i" % (depth+1))

        # add space to each node
        output.seek(0)
        pad_length = 3
        keys = []
        spaces = int(math.pow(2, depth))

        while spaces > 0:
            skip_start = spaces * pad_length
            skip_mid = (2 * spaces - 1) * pad_length

            key_start_spacing = ' ' * skip_start
            key_mid_spacing = ' ' * skip_mid

            keys = output.readline().split(' ')  # read one level to parse
            padded_keys = (add_padding(key, pad_length) for key in keys)
            padded_str = key_mid_spacing.join(padded_keys)
            complete_str = ''.join([key_start_spacing, padded_str])

            pretty_output.write(complete_str)

            # add space and slashes to middle layer
            slashes_depth = spaces
            # print('current slashes depth is:')
            # print(spaces)
            # print("current levle's list is:")
            # print(keys)
            spaces = spaces // 2
            if spaces > 0:
                pretty_output.write('\n')  # print '\n' each level

                cnt = 0
                while cnt < slashes_depth:
                    inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                    symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                    symbol_start_spacing = ' ' * (skip_start - cnt - 1)
                    symbol_mid_spacing = ' ' * (skip_mid - 2 * (cnt + 1))
                    pretty_output.write(''.join([symbol_start_spacing, symbol]))
                    for i in keys[1:-1]:
                        pretty_output.write(''.join([symbol_mid_spacing, symbol]))
                    pretty_output.write('\n')
                    cnt = cnt + 1

        print(pretty_output.getvalue())


if __name__ == '__main__':
    # initialize the tree
    tree = TreeNode(1,
                    TreeNode(2,
                             TreeNode(4,
                                      TreeNode(7, None, None),
                                      None),
                             TreeNode(5, None, None)),
                    TreeNode(3,
                             TreeNode(6,
                                      TreeNode(8, None, None),
                                      TreeNode(9, None, None)),
                             None))
    tree_array = [5, 1, 2, 0, None, 3, 4, None, None, 6]
    tree = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(tree)
