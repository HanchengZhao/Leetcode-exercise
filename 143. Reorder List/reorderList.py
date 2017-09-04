# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        # find the middle node 
        fast = head
        slow = head
        if fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half   1-2-3-4-5-6  -> 1-2-3-6-5-4 # mid will be at the 6
        mid = slow.next
        curr = mid.next
        while curr:
            nexttemp = curr.next
            curr.next = mid
            mid = curr
            curr = nexttemp
        # 1->2->3->4<-5<-6
        # reorder the list
        p1, p2 = head, mid
        while p1 != p2:
            mid.next = p2.next # record p2.next first
            p2.next = p1.next # change the p2 pointer to p1 next
            p1.next = p2 # let p1 point to p2
            p1 = p2.next # move p1 to next
            p2 = mid.next # move p2 to next

