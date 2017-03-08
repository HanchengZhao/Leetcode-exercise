# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        head = dummy
        while l1 or l2:
            if not l1:
                head.next = ListNode((l2.val+carry) % 10)
                carry = (l2.val+carry) / 10
                head = head.next
                l2 = l2.next
            elif not l2:
                head.next = ListNode((l1.val+carry) % 10)
                carry = (l1.val+carry) / 10
                head = head.next
                l1 = l1.next
            else:
                sum = (l1.val+l2.val+carry) % 10
                head.next = ListNode(sum)
                carry = (l1.val+l2.val+carry) / 10
                head = head.next
                l1 = l1.next
                l2 = l2.next
        if carry:
            head.next = ListNode(carry)
        return dummy.next