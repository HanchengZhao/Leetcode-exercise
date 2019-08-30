class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for i in range(n)] for j in range(m)]
        # right down corner is obstacle
        if dp[-1][-1] == 1:
            return 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == m-1 and j == n-1:
                    dp[i][j] = 1
                else:
                    right = dp[i][j+1] if j+1 < n else 0
                    down = dp[i+1][j] if i+1 < m else 0
                    dp[i][j] = right + down
        return dp[0][0]
