class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = [[0] * (n+1) for i in xrange(m+1)]
        #fill first row
        for i in xrange(n):
            if i == 0:
                res[0][i] = grid[0][i]
            else:
                res[0][i] = grid[0][i] + res[0][i-1]
        #fill first column
        for j in xrange(m):
            if j:
                res[j][0] = grid[j][0] + res[j-1][0]

        for i in xrange(1, m):
            for j in xrange(1, n):
                res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        return res[m-1][n-1]

s = Solution()
print s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])