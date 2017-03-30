class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 2
        for i in xrange(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[n-1]