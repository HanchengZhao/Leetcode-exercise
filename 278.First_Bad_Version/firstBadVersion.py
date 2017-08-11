# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.biSearch(1, n)
        
    def biSearch(self, i, j):  
        if i == j:
            return i
        mid = (i + j) / 2
        if isBadVersion(mid):
            if not isBadVersion(mid-1):
                return mid
            self.biSearch(i, mid)
        else:
            if isBadVersion(mid+1):
                return mid+1
            self.biSearch(mid, j)

# this version will have a infinity loop for (1, 2) if 2 is bad
    # def biSearch(self, i, j):  
    #     if i == j:
    #         return i
    #     mid = (i + j) / 2
    #     if isBadVersion(mid):
    #         self.biSearch(i, mid)
    #     else:
    #         self.biSearch(mid, j)