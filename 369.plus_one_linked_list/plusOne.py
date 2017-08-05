# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
reverse the list and add 1 and reverse back

'''
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return ListNode(1)
        newHead = self.reverse(head)
        pointer = newHead
        carry = 0
        pointer.val += 1
        while pointer:
            val = pointer.val + carry
            carry = val / 10
            pointer.val = val % 10
            if carry == 0:
                break
            prev = pointer # keep track of the last Node that has value
            pointer = pointer.next
        if carry == 1: # deal with the last carry
            prev.next = ListNode(1)
        return self.reverse(newHead)


    def reverse(self, head):
        dummy = ListNode(None)
        while head:
            temp = dummy.next # insert head between temp and dummy
            dummy.next = ListNode(head.val)
            dummy.next.next = temp
            head = head.next
        return dummy.next