# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        cur_node = root
        while cur_node:
            length += 1
            cur_node = cur_node.next
        result = []
        part_base_len = length // k
        p1 = length % k
        p0 = k - p1
        cur_node = root
        for i in range(p1):
            head = None
            c_node = None
            for j in range(part_base_len + 1):
                if not head:
                    head = ListNode(cur_node.val)
                    c_node = head
                else:
                    c_node.next = ListNode(cur_node.val)
                    c_node = c_node.next
                cur_node = cur_node.next
            result.append(head)
        for i in range(p0):
            if cur_node:
                head = None
                c_node = None
                for j in range(part_base_len):
                    if cur_node:
                        if not head:
                            head = ListNode(cur_node.val)
                            c_node = head
                        else:
                            c_node.next = ListNode(cur_node.val)
                            c_node = c_node.next
                        cur_node = cur_node.next
                result.append(head)
            else:
                result.append([])
        return result


def main(*args):
    solution = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    k2 = 3
    root = ListNode(arr2[0])
    cur_node = root
    for k, v in enumerate(arr2):
        if k > 0:
            cur_node.next = ListNode(v)
            cur_node = cur_node.next

    result = solution.splitListToParts(root, k2)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
