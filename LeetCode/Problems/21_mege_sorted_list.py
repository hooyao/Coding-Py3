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
    def mergeTwoLists_slow(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    #slow too
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


def main(*args):
    solution = Solution()

    l1 = gen_list([2,4,6])
    l2 = gen_list([1,3,5])
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
