# Definition for singly-linked list.
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

        def nextNode(l1, l2, addup):
            sumup = l1.val + l2.val + addup
            if -10 < sumup < 10:
                addup = 0
                thisNode = ListNode(sumup)
            else:
                addup = (sumup - sumup % 10) / 10
                thisNode = ListNode(sumup % 10)
            if l1.next is not None and l2.next is not None:
                thisNode.next = nextNode(l1.next, l2.next, addup)
            elif l1.next is None and l2.next is not None:
                thisNode.next = nextNode(ListNode(0), l2.next, addup)
            elif l1.next is not None and l2.next is None:
                thisNode.next = nextNode(l1.next, ListNode(0), addup)
            elif addup != 0:
                thisNode.next = nextNode(ListNode(0), ListNode(0), addup)
            return thisNode

        return nextNode(l1, l2, 0)
