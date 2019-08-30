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
        # 1->2->3->2->1->None, fast = 5, slow = 3
        #1->2->3->4->2->1->None, fast = None, slow = 4
        # if the # of nodes is odd, slow is the middle one, if the 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow = self.reverseList(slow) 
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
'''
reverse from the middle and start checking
'''
            
            
            
    
            