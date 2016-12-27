# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
   
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
            
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = self.reverseList(slow.next)
        slow = slow.next
        while slow:
            if slow.val != head.val:
                return False
            head = head.next
            slow = slow.next
        return True
     
    def reverseList(self, head):
            newHead = None
            while head:
                Next = head.next
                head.next = newHead
                newHead = head
                head = Next
            return newHead   
        
            
            
            
    
            