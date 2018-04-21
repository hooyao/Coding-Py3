import sys


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        run_pos = self.run(None, head, n)
        if run_pos == n:
            return head.next
        return head

    def run(self, parent, node, n):
        if not node.next:
            cur_pos_from_tail = 1
        else:
            cur_pos_from_tail = self.run(node, node.next, n) + 1
        if cur_pos_from_tail == n and parent:
            parent.next = node.next
        return cur_pos_from_tail


def main(*args):
    arr = [1]
    n = 1
    head = ListNode(arr[0])
    cur_node = head
    for k, v in enumerate(arr):
        if k > 0:
            cur_node.next = ListNode(v)
            cur_node = cur_node.next

    solution = Solution()
    result = solution.removeNthFromEnd(head, n)

    cur_node = result
    while cur_node:
        print(cur_node.val)
        cur_node = cur_node.next

    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
