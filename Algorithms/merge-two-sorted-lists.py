# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def merge(l1, l2):
            if l1 is None and l2 is not None:
                root = ListNode(l2.val)
                root.next = merge(None, l2.next)
                return root
            elif l1 is not None and l2 is None:
                root = ListNode(l1.val)
                root.next = merge(l1.next, None)
                return root
            elif l1 is None and l2 is None:
                return
            else:
                if l1.val >= l2.val:
                    root = ListNode(l2.val)
                    if l2.next is None:
                        root.next = merge(l1, None)
                        return root
                    if l1.val >= l2.next.val:
                        root.next = merge(l1, l2.next)
                    else:
                        root.next = merge(l1, l2.next)
                else:
                    root = ListNode(l1.val)
                    if l1.next is None:
                        root.next = merge(None, l2)
                        return root
                    if l2.val >= l1.next.val:
                        root.next = merge(l1.next, l2)
                    else:
                        root.next = merge(l1.next, l2)
                return root

        return merge(l1, l2)
