class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        # count all the 1s
        self.count = sum([grid[i][j] == "1" for i in range(row)
                          for j in range(col)])
        # point each one to itself initially
        parents = [i for i in range(row * col)]
        # find

        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return parents[x]
        # union

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return
            parents[xroot] = yroot
            self.count -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] != "1":
                    continue
                index = i * col + j
                # right side
                if j < col - 1 and grid[i][j+1] == "1":
                    union(index, index + 1)
                # down
                if i < row - 1 and grid[i+1][j] == "1":
                    union(index, index + col)
        return self.count
