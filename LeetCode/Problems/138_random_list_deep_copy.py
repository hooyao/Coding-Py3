import sys


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        new_head = RandomListNode(head.label)
        cur_node = head
        new_cur_node = new_head
        node_dict = dict()
        node_dict[head] = new_head
        while cur_node.next is not None:
            next_node = cur_node.next
            new_cur_node.next = RandomListNode(next_node.label)
            node_dict[next_node] = new_cur_node.next
            cur_node = next_node
            new_cur_node = new_cur_node.next

        cur_node = head
        while cur_node is not None:
            correspond_new_node = node_dict[cur_node]
            if cur_node.random is not None:
                correspond_new_node.random = node_dict[cur_node.random]
            else:
                correspond_new_node.random = None
            cur_node = cur_node.next

        return new_head


def main(*args):
    solution = Solution()
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.random = head
    result = solution.copyRandomList(head)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
