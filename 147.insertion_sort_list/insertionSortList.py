# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        cur = head
        while cur:
            temp = dummy # the pos to insert
            while temp.next and temp.next.val < cur.val:
                temp = temp.next
            curNext = cur.next # save the original list pointer
            cur.next = temp.next
            temp.next = cur
            cur = curNext
        return dummy.next