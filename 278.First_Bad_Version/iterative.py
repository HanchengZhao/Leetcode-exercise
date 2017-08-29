class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            if i == j: # edge case for equals
                return i
            mid = (i + j) / 2
            if isBadVersion(mid):
                if mid-1 > 0 and not isBadVersion(mid-1): # check backward
                    return mid
                else: 
                    j = mid
            else: # not bad version
                if mid+1 <= n and isBadVersion(mid+1): # check forward
                    return mid+1
                else:
                    i = mid
'''
use binary search to check the bad one, whenever check the mid, check one more step forward or
backward to ensure if found the first bad version
'''