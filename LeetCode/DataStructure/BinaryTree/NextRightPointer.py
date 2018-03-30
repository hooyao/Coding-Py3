class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or (not root.left and not root.right):
            return root

        strut = dict()
        level_0 = [root]
        lv = 0
        strut[lv] = level_0
        is_last_level = False
        while not is_last_level:
            new_level = []
            last_node = None
            is_last_level = True
            for ele in strut[lv]:
                if last_node:
                    last_node.next = ele
                last_node = ele
                is_last_level = is_last_level and (ele.left is None)
                new_level.append(ele.left)
                is_last_level = is_last_level and (ele.right is None)
                new_level.append(ele.right)
            lv += 1
            strut[lv] = new_level
        return root

    def has_less_then_one_gen(self, parent):
        left = parent.left
        right = parent.right
        if left and self.has_kids(left):
            return False
        if right and self.has_kids(right):
            return False
        return True

    def has_kids(self, parent):
        return parent.left or parent.right
