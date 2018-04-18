# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        elif not head.next:
            return head

        runner0 = head
        runner1 = head.next
        runner0_last = None
        while runner1:
            if runner0.val == runner1.val:
                while runner1.next and runner1.val == runner0.val:
                    runner1 = runner1.next
                if runner0.val == runner1.val:
                    runner1 = None
                if runner0_last:
                    runner0_last.next = runner1
                else:
                    head = runner1
                runner0 = runner1
                runner1 = runner1.next if runner1 else None

            else:
                runner0_last = runner0
                runner0 = runner1
                runner1 = runner1.next
        return head


def main(*args):
    values = [1, 2,2,2]
    head = ListNode(values[0])
    cur_node = head
    for idx in range(1, len(values)):
        cur_node.next = ListNode(values[idx])
        cur_node = cur_node.next

    solution = Solution()
    result = solution.deleteDuplicates(head)
    cur_node = result
    while cur_node:
        print(str(cur_node.val))
        cur_node = cur_node.next


if __name__ == '__main__':
    main(*sys.argv[1:])
