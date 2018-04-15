import sys

from BTreeUtils import BTreeHelper, TreeNode


class Solution:

    def serialize(self, root):
        arr = []
        self.preoder_t(root, arr)
        result = ''
        for idx, ele in enumerate(arr):
            result += str(ele)
            if idx < len(arr) - 1:
                result += ','
        return result

    def preoder_t(self, root, arr):
        if not root:
            return
        arr.append(root.val)
        self.preoder_t(root.left, arr)
        self.preoder_t(root.right, arr)

    def deserialize(self, data):
        arr = list(map(int, data.split(',')))
        return self.deserialize_rec(arr, 0, len(arr) - 1)

    def deserialize_rec(self, arr, start, end):
        this_root = TreeNode(arr[start])
        if start == end:
            return this_root
        mid = arr[start]
        if arr[start + 1] >= mid:
            right_part = self.deserialize_rec(arr, start + 1, end)
            this_root.right = right_part
            return this_root
        if arr[end] <= mid:
            left_part = self.deserialize_rec(arr, start + 1, end)
            this_root.left = left_part
            return this_root
        idx = start + 1

        while arr[idx] < mid and idx < len(arr):
            idx += 1
        left_part = self.deserialize_rec(arr, start + 1, idx - 1)
        right_part = self.deserialize_rec(arr, idx, end)
        this_root.left = left_part
        this_root.right = right_part
        return this_root


def main(*args):
    tree_array = [10, 5, 15, 2, 6, 12, None, None, None, None, 7, None, 13]
    root = BTreeHelper.list_to_tree(tree_array)
    BTreeHelper.pretty_print(root)
    solution = Solution()
    data = solution.serialize(root)
    print(data)
    node = solution.deserialize(data)
    print(BTreeHelper.pretty_print(node))


if __name__ == '__main__':
    main(*sys.argv[1:])
