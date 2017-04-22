# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h1 = head
        vals = []
        while h1:
            vals.append(h1.val)
            h1 = h1.next
        vals.sort()
        h2 = head
        for val in vals:
            h2.val = val
            h2 = h2.next
        return head