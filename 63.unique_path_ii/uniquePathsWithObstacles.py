class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 1

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0]*(n+1) for i in xrange(m+1)]
        res[m-1][n-1] = 1 if not obstacleGrid[m-1][n-1] else 0
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if i != m-1 or j != n-1:
                    res[i][j] = 0 if obstacleGrid[i][j] else res[i+1][j]+res[i][j+1]
        return res[0][0]
s = Solution()
print s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])