class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                else:
                    left = dp[i][j-1] if j-1 >= 0 else float("inf")
                    up = dp[i-1][j] if i-1 >= 0 else float("inf")
                    dp[i][j] = grid[i][j] + min(left, up)
        return dp[-1][-1]
