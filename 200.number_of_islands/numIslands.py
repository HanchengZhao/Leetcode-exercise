class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for i in xrange(rows)]
        islands = 0
        for i in xrange(rows):
            for j in xrange(cols):
                if visited[i][j] == False and grid[i][j] == "1":
                    self.dfs(i, j, visited, rows, cols)
                    islands += 1
        return islands

    def dfs(self, i, j, visited, rows, cols):
        visited[i][j] = True
        rowNbr = [-1,0,0,1]
        colNbr = [0,-1,1,0]
        for k in xrange(4):
            row = i + rowNbr[k]
            col = j + colNbr[k]
            if row >= 0 and row < rows and col >= 0 and col < cols and not visited[row][col]: # safe area
                self.dfs(row, col, visited, rows, cols)
#maximum recursion depth exceeded
s = Solution()
print s.numIslands(["11110","11010","11000","00000"])