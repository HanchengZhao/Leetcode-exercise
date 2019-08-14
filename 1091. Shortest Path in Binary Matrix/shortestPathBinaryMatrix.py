from typing import List
# My first idea here is to use dp to solve, but the trick part is that we don't
# know the direcation of the path, so we can't traverse from top-left to bottom right
# to get the minimum path

# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         l = len(grid)
#         # check the start and end point
#         if grid[0][0] != 0 or grid[l-1][l-1] != 0:
#             return -1
#         count = [[l**2] * (len(grid) + 2) for i in range(len(grid) + 2)]
#         count[0][0] = 0
#         for i in range(len(grid)):
#             for j in range(len(grid)):
#                 if grid[i][j] == 0:
#                     count[i+1][j+1] = min(count[i][j], count[i][j+1], count[i][j+2], count[i+1]
#                                           [j], count[i+1][j+2], count[i+2][j], count[i+2][j+1], count[i+2][j+2]) + 1
#         return count[-2][-2] if count[-2][-2] <= l**2 else -1

# we have to use bfs to solve it

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        l = len(grid)
        if grid[0][0] != 0 or grid[l-1][l-1] != 0:
            return -1
        queue = deque()
        visited = [[-1] * l for i in range(l)]
        visited[0][0] = 1
        # [x, y]
        queue.append([0, 0])
        while len(queue) != 0:
            pt = queue.popleft()
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if pt[0] + i >= 0 and pt[0] + i < l and pt[1] + j >= 0 and pt[1] + j < l:
                        x = pt[0] + i
                        y = pt[1] + j
                        if grid[x][y] == 0 and visited[x][y] == -1:
                            queue.append([x, y])
                            visited[x][y] = visited[pt[0]][pt[1]] + 1

        return visited[-1][-1]
