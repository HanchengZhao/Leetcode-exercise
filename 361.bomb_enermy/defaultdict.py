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
from collections import defaultdict
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        enemy_row = defaultdict(list)
        enemy_col = defaultdict(list)
        wall_row = defaultdict(list)
        wall_col = defaultdict(list)
        empty = []
        res = 0
        #initialize
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "E":
                    enemy_row[i].append(j)
                    enemy_col[j].append(i)
                elif grid[i][j] == "W":
                    wall_row[i].append(j)
                    wall_col[j].append(i)
                else:
                    empty.append((i,j))
        for row, col in empty:
            count = 0
            e_r = enemy_row[row]
            e_c = enemy_col[col]
            w_r = wall_row[row]
            w_c = wall_col[col]
            for i in e_r:
                stop = 0
                for j in w_r:
                    if (j > i and j < row) or (j > row and j < i):
                        stop = 1
                        break
                if not stop: count += 1

            for i in e_c:
                stop = 0
                for j in w_c:
                    if (j > i and j < row) or (j > row and j < i):
                        stop = 1
                        break
                if not stop: count += 1
            res = max(res, count)
        print enemy_row,enemy_col,wall_col,wall_row
        return res
#test case not passed
s = Solution()
print s.maxKilledEnemies(["0E00","E0WE","0E00"])