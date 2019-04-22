# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        faster = slower = head
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                return True
        return False
