class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        tmp = slow.next
        slow.next = None
        slow = tmp
        
        slow = self.reverseLinkedList(slow)
        cur = head
        while slow:
            tmp = slow.next
            slow.next = cur.next
            cur.next = slow
            cur = slow.next
            slow = tmp
            
    
    def reverseLinkedList(self, head):
        prev = None
        cur = head
        
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev