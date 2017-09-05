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
            heapq.heappush(h, i)
            if len(h) > k: # if the size if bigger than k, pop the smallest one
                heapq.heappop(h)
        return h[0]
    # time: O(nlog(k)), space: O(k)