# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None, return None
        if not head:
            return None
        # if there is only one node, return the node
        if not head.next:
            return head
        # if there is 2 nodes, return the second one
        if not head.next.next:
            return head.next
        # normal: fast node moves 2 steps first, then slow node moves 1 step until
        # faster reaches the end, then decide whether the slow moves forward 1 step
        # further to mark the middle
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            slow = slow.next
        return slow
