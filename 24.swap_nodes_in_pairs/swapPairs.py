# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        former = dummy
        while head and head.next:
            #record the next node
            nextnode = head.next.next
            #swap nodes, start from former
            former.next = head.next
            head.next.next = head
            head.next = nextnode

            former = former.next.next
            head = nextnode
        # no head.next
        if head:
            former.next = head
        return dummy.next
