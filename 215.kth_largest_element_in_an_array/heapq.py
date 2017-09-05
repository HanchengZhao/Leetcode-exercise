import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for i in nums:
            heapq.heappush(h, -i)
        for j in xrange(k):
            res = -heapq.heappop(h)
        return res