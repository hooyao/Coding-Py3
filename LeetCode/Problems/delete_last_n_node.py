#!/usr/bin/env python
"""
@author:hooyao
@license: Apache Licence
@file: delete_last_n_node
@time: 3/26/2019
@contact: hooyao@gmail.com
@site:
@software: PyCharm

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
    def delete_node(self, head: ListNode, last_n: int) -> ListNode:
        head, count = self.count_delete(head, last_n)
        return head

    def count_delete(self, head: ListNode, last_n: int) -> (ListNode, int):
        if not head.next:
            if last_n > 1:
                return head, 1
            else:
                return None, -1
        next_head, rest_count = self.count_delete(head.next, last_n)
        if rest_count > 0:
            count = rest_count + 1
            if count == last_n:
                head = next_head
                count = -1
            return head, count
        else:
            head.next = next_head
            return head, -1


def main(*args):
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    head = None
    current = None
    for v in values:
        if current is None:
            current = ListNode(v)
            head = current
        else:
            current.next = ListNode(v)
            current = current.next

    new_head = Solution().delete_node(head, 10)
    while new_head is not None:
        print(str(new_head) + "\n")
        new_head = new_head.next


if __name__ == '__main__':
    main(*sys.argv[1:])
