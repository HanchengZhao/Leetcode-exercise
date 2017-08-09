class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0]) if m else 0
        #does not match
        if r * c != m * n :
            return nums
        temp = []
        for i in xrange(m):
            for j in xrange(n):
                temp.append(nums[i][j])
        res = [[0] * c for i in xrange(r)]
        for i in xrange(r):
            for j in xrange(c):
                res[i][j] = temp.pop(0)
        return res
