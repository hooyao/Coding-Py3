#!/usr/bin/env python
"""
@author:hooyao
@license: Apache Licence
@file: 206_reverse_linked_list
@time: 2019/03/26
@site:
@software: PyCharm

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""
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
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            next_head = head.next
            head.next = None
            while next_head:
                tmp = head
                head = next_head
                next_head = next_head.next
                head.next = tmp
        return head


def main(*args):
   # values = [1, 2, 3, 4]
    #values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #values = [1]
    values = []
   # values = [1,2]
    head = None
    current = None
    for v in values:
        if current is None:
            current = ListNode(v)
            head = current
        else:
            current.next = ListNode(v)
            current = current.next
    new_head = Solution().reverseList(head)
    while new_head is not None:
        print(str(new_head) + "\n")
        new_head = new_head.next


if __name__ == '__main__':
    main(*sys.argv[1:])
