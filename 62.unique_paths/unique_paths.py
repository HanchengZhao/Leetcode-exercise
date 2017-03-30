class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0]*(n) for i in xrange(m)]
        res[m-1][n-1] = 1
        for x in xrange(m-1,-1,-1):
            for y in range(n-1,-1,-1):
                if x != m-1 or y !=n-1:
                    right = 0 if (y+1) > n-1 else res[x][y+1]
                    down =  0 if (x+1) > m-1 else res[x+1][y]
                    res[x][y] = right + down
        return res[0][0]
s = Solution()
print s.uniquePaths(1,2)
