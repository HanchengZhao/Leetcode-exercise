import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for node in lists:
            while node:
                heapq.heappush(h, node.val)
                node = node.next
        dummy = ListNode(0)
        head = dummy
        while h:
            head.next = ListNode(heapq.heappop(h))
            head = head.next
        return dummy.next
'''
rather than saving node, just push all val to heap
'''