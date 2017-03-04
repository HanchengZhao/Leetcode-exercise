class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        hindex = 0
        for i in xrange(n):
            hindex = max(hindex, min(citations[i], n - i))
        return hindex
s = Solution()
print s.hIndex([3, 0, 6, 1, 5])