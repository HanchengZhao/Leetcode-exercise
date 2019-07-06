class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, grid)
        return count

    # change the connected islands to water field
    def dfs(self, x, y, grid):
        grid[x][y] = '0'
        m, n = len(grid), len(grid[0])
        rows = [-1, 0, 0, 1]
        cols = [0, 1, -1, 0]
        for i in range(4):
            x1, y1 = x + rows[i], y + cols[i]
            if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == '1':
                self.dfs(x + rows[i], y+cols[i], grid)
