'''
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
'''

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0]) if m else 0
        max_killed = 0
        row_e = 0
        col_e = [0] * n
        for row in range(m):
            for col in range(n):
                # do not recalculate enemies if there is no wall
                if not col or grid[row][col-1] == "W":
                    row_e = 0
                    for cl in range(col, n): #keep counting enermies in this row until meeting a wall
                        if grid[row][cl] == "W" : break
                        row_e += grid[row][cl] == "E"

                if not row or grid[row-1][col] == "W":
                    col_e[col] = 0
                    for ro in range(row, m):
                        if grid[ro][col] == "W": break
                        col_e[col] += grid[ro][col] == "E"

                if grid[row][col] == "0":
                    max_killed = max(max_killed, row_e + col_e[col])

        return max_killed

s = Solution()
print s.maxKilledEnemies(["0E00","E0WE","0E00"])