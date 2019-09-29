class Solution:
    def minimumMoves(self, grid) -> int:
        # 0 = horizontal, 1 = vertical
        n = len(grid)
        dp = [[[float("inf"), float("inf")] for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = 0
        # init first row 
        for i in range(1, n-1):
            if grid[0][i+1] == 0:
                dp[0][i][0] = dp[0][i-1][0] + 1
            else:
                break # no need to check the rest columns
        for i in range(n):
            for j in range(n):
                if j < n - 1 and grid[i][j + 1] == 0:
                    dp[i][j][0] = min(dp[i][j][0], dp[i][j - 1][0] + 1)
                    if grid[i][j] == 0:
                        dp[i][j][0] = min(dp[i][j][0],dp[i - 1][j][0] + 1)
                if i < n - 1 and grid[i + 1][j] == 0:
                    dp[i][j][1] = min(dp[i][j][1], dp[i - 1][j][1] + 1)
                    if grid[i][j] == 0:
                        dp[i][j][1] = min(dp[i][j][1], dp[i][j - 1][1] + 1)
                if i < n - 1 and j < n - 1 and grid[i][j + 1] == grid[i + 1][j] == grid[i + 1][j + 1] == 0:
                    dp[i][j][0], dp[i][j][1] = min(dp[i][j][0], dp[i][j][1] + 1), min(dp[i][j][1], dp[i][j][0] + 1)
        return dp[n - 1][n - 2][0] if dp[n - 1][n - 2][0] < float('inf') else -1

s = Solution()
print(s.minimumMoves([[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]))

print(s.minimumMoves([[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]))