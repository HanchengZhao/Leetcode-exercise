# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        dummy = ListNode(0)
        head = dummy
        pq = []
        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, node))
        while pq:
            nextnode = heapq.heappop(pq)
            n = nextnode[1]
            head.next = n
            head = head.next
            if n.next:
                n = n.next
                heapq.heappush(pq, (n.val, n))
        return dummy.next