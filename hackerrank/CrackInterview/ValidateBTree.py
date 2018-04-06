import BTreeUtils


def checkBST(root):
    is_bst, min, max = recursive_check(root)
    return is_bst

def recursive_check(root):
    if not root.left and not root.right:
        return True, root.data, root.data
    bst_left, bst_right = True, True
    this_min = root.data
    this_max = root.data
    if root.left:
        rec_left, min_left, max_left = recursive_check(root.left)
        bst_left = root.data > max_left and rec_left
        if bst_left:
            this_min = min_left
    if root.right:
        rec_right, min_right, max_right = recursive_check(root.right)
        bst_right = root.data < min_right and rec_right
        if bst_right:
            this_max = max_right
    return bst_left and bst_right, this_min, this_max


root = BTreeUtils.BTreeHelper.list_to_tree([4, 2, 6, 1, 3, 5, 7])
BTreeUtils.BTreeHelper.pretty_print(root)
print(checkBST(root))
