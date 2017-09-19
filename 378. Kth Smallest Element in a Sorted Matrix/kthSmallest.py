class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) / 2
            count = 0 # count how many elements is smaller than k
            l = len(matrix) # row length
            col = l-1
            for i in xrange(l): # loop row by row
                while col >= 0:
                    if matrix[i][col] > mid:
                        col -= 1
                    else:
                        break
                count += col + 1 # add # of elements that is smaller than mid
            if count < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
s = Solution()
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
'''
use a binary search to find the mid of the array, 
count the number of elements that are smaller than mid from the end of the row,
check whether it is k, otherwise change the range
'''