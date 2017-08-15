class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i,j,grid):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i-1, j, grid)
            dfs(i, j+1, grid)
            dfs(i, j-1, grid)
            dfs(i+1, j, grid)

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for i in xrange(rows):
            for j in xrange(cols):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    islands += 1
        return islands

    