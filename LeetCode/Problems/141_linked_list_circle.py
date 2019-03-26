#!/usr/bin/env python
"""
@author:hooyao
@license: Apache Licence
@file: 141_linked_list_circle
@time: 3/26/2019
@contact: hooyao@gmail.com
@site:
@software: PyCharm

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

"""
import sys


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def hasCycle(self, head):
        if head and head.next:
            runner_one = head
            runner_two = head
            while runner_one.next and runner_two.next and runner_two.next.next:
                runner_one = runner_one.next
                runner_two = runner_two.next.next
                if runner_two == runner_one or runner_two.next == runner_one:
                    return True
        return False


def main(*args):
    values = [1, 2]
    loop_pos = 0
    loop_node = None
    head = None
    current = None
    for idx, v in enumerate(values):
        if current is None:
            current = ListNode(v)
            head = current
        else:
            current.next = ListNode(v)
            current = current.next
        if idx == loop_pos:
            loop_node = current
        if idx == len(values) - 1:
            current.next = loop_node

    print(Solution().hasCycle(head))


if __name__ == '__main__':
    main(*sys.argv[1:])
