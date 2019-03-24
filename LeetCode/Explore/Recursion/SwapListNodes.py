#!/usr/bin/env python  
""" 
@author:shz 
@license: Apache Licence 
@file: SwapListNodes.py 
@time: 2019/03/25
@contact: sunhouzan@163.com
@site:  
@software: PyCharm

Given 1->2->3->4, you should return the list as 2->1->4->3.


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
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            swap_l = head
            swap_r = head.next
            swap_l.next = self.swapPairs(swap_r.next)
            swap_r.next = swap_l
            return swap_r
        return head

def main(*args):
    values = [1, 2, 3, 4]
    head = None
    current = None
    for v in values:
        if current is None:
            current = ListNode(v)
            head = current
        else:
            current.next = ListNode(v)
            current = current.next
    new_head = Solution().swapPairs(head)

    while new_head is not None:
        print(str(new_head) + "\n")
        new_head = new_head.next


if __name__ == '__main__':
    main(*sys.argv[1:])
