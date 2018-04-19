# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and not l2:
            return l1
        if not l1 and l2:
            return l2
        head = None
        cur_node = None
        if l1 and l2:
            cur_l1 = l1
            cur_l2 = l2
            while cur_l1 or cur_l2:
                if cur_l1 and cur_l2:
                    if cur_l1.val <= cur_l2.val:
                        min_val = cur_l1.val
                        cur_l1 = cur_l1.next
                    else:
                        min_val = cur_l2.val
                        cur_l2 = cur_l2.next
                    if not head:
                        cur_node = ListNode(min_val)
                        head = cur_node
                    else:
                        cur_node.next = ListNode(min_val)
                        cur_node = cur_node.next
                elif cur_l1:
                    if not head:
                        cur_node = ListNode(cur_l1.val)
                        head = cur_node
                    else:
                        cur_node.next = ListNode(cur_l1.val)
                        cur_node = cur_node.next
                    cur_l1 = cur_l1.next
                else:
                    if not head:
                        cur_node = ListNode(cur_l2.val)
                        head = cur_node
                    else:
                        cur_node.next = ListNode(cur_l2.val)
                        cur_node = cur_node.next
                    cur_l2 = cur_l2.next
        return head


def main(*args):
    solution = Solution()

    l1 = gen_list([])
    l2 = gen_list([1])
    result = solution.mergeTwoLists(l1, l2)
    print(result)


def gen_list(arr):
    cur_node = None
    head = None
    for ele in arr:
        if not head:
            head = ListNode(ele)
            cur_node = head
        else:
            cur_node.next = ListNode(ele)
            cur_node = cur_node.next
    return head


if __name__ == '__main__':
    main(*sys.argv[1:])
