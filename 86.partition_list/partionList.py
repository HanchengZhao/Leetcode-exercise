# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast and fast.next:
            if fast.next.val < x:
                if fast == slow: # for the corner case
                    fast = fast.next
                    slow = slow.next
                else:
                    #record node
                    moveNode = fast.next
                    fast.next = moveNode.next
                    #add after slow
                    moveNode.next = slow.next
                    slow.next = moveNode
                    slow = slow.next
            else:
                fast = fast.next
        return dummy.next
