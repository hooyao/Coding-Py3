import sys


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tail1 = l1
        tail2 = l2
        digit = l1.val + l2.val
        bring_over = int(digit / 10)
        digit = digit % 10
        result = ListNode(digit)
        result_tail = result
        while tail1.next or tail2.next or bring_over > 0:
            t1d = 0
            t2d = 0
            if tail1.next:
                t1d = tail1.next.val
                tail1 = tail1.next
            if tail2.next:
                t2d = tail2.next.val
                tail2 = tail2.next
            digit = t1d + t2d + bring_over
            bring_over = int(digit / 10)
            digit = digit % 10
            result_tail.next = ListNode(digit)
            result_tail = result_tail.next
        return result

    def from_number(self, number):
        head = ListNode(int(number % 10))
        tail = head
        tmp = int(number / 10)
        while tmp / 10 > 0:
            digit = int(tmp % 10)
            tmp = int(tmp / 10)
            tail.next = ListNode(digit)
            tail = tail.next
        return head

    def to_number(self, head):
        tail = head
        result = tail.val
        multiplier = 10
        while tail.next is not None:
            result += tail.next.val * multiplier
            multiplier = multiplier * 10
            tail = tail.next
        return result


def main(*args):
    solution = Solution()
    l1 = solution.from_number(5)
    l2 = solution.from_number(5)
    result = solution.addTwoNumbers(l1, l2)
    print(solution.to_number(result))


if __name__ == '__main__':
    main(*sys.argv[1:])
