# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: # or head.next is None
            return True
        slow = head
        fast = head
        # slow will reach the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        print slow.val
        slow.next = self.reverse(slow.next)
        slow = slow.next
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
        
    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            nxt = head.next
            head.next = prev
            prev = cur
            cur = nxt
        return prev