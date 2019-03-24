import sys

from BTreeUtils import BTreeHelper


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.current_node = root
        self.stack = []
        while self.current_node and self.current_node.left:
            self.stack.append(self.current_node)
            self.current_node = self.current_node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.current_node else False

    def next(self):
        """
        :rtype: int
        """
        result = self.current_node.val
        if self.current_node.right:
            self.current_node = self.current_node.right
            while self.current_node.left:
                self.stack.append(self.current_node)
                self.current_node = self.current_node.left
        else:
            if len(self.stack) > 0:
                parent = self.stack[-1]
                self.current_node = parent
                self.stack.pop()
            else:
                self.current_node = None
        return result


def main(*args):
    tree_array = [10, 5, 14, 3, 7, None, None, 2, 4]
    none_tree = []
    root = BTreeHelper.list_to_tree(none_tree)
    BTreeHelper.pretty_print(root)
    itr = BSTIterator(root)
    while itr.hasNext():
        print(itr.next())

if __name__ == '__main__':
    main(*sys.argv[1:])
