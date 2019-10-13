class Solution:
    def getMaximumGold(self, grid):
        m, n = len(grid), len(grid[0])
        cached = [[-1 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(matrix, i, j, cached, visited, m, n):
            if cached[i][j] != -1:
                return cached[i][j]
            directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
            maximum = 0
            # visiting
            visited[i][j] = True
            for d in directions:
                nx = i + d[0]
                ny = j + d[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or cached[nx][ny] != -1 or visited[i][j]:
                    continue
                maximum = max(maximum, dfs(
                    matrix, nx, ny, cached, visited, m, n))
            cached[i][j] = maximum + matrix[i][j]
            return cached[i][j]
        longest = 0
        for i in range(m):
            for j in range(n):
                longest = max(longest, dfs(grid, i, j, cached, visited, m, n))
        print(cached)
        return longest


s = Solution()
print(s.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
