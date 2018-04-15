"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    if head is None:
        return False
    runner1 = head
    runner2 = head
    while True:
        if runner1.next is None:
            return False
        runner1 = runner1.next
        if runner2.next is None or runner2.next.next is None:
            return False
        runner2 = runner2.next.next
        if runner1 == runner2:
            return True


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next
print(has_cycle(head))
