class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, leng = 0, len(citations)
        right = leng-1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] == leng - mid:
                return citations[mid]
            elif citations[mid] > leng - mid:
                right = mid-1
            else:
                left = mid+1
        return leng - (right+1)



s = Solution()
print s.hIndex([3, 0, 6, 1, 5])


