"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        node = Node()
        # print(grid)
        if len(grid) == 1:
            node.val = grid[0][0]
            node.isLeaf = True
        else:
            n = len(grid)
            node.topLeft = self.construct(
                self.getSubGrid(0, n//2, 0, n // 2, grid))
            node.topRight = self.construct(
                self.getSubGrid(0, n//2, n // 2, n, grid))
            node.bottomLeft = self.construct(
                self.getSubGrid(n//2, n, 0, n // 2, grid))
            node.bottomRight = self.construct(
                self.getSubGrid(n//2, n, n // 2, n, grid))
            if node.topLeft.isLeaf and \
                    node.topRight.isLeaf and \
                    node.bottomLeft.isLeaf and \
                    node.bottomRight.isLeaf and \
                    node.topLeft.val == node.topRight.val \
                    == node.bottomLeft.val == node.bottomRight.val:
                node.isLeaf = True
                node.val = node.topLeft.val
                node.topLeft = node.topRight = node.bottomLeft = node.bottomRight = None
        return node

    def getSubGrid(self, srow, erow, scol, ecol, grid):
        res = [[0 for _ in range(scol, ecol)] for _ in range(srow, erow)]
        for i in range(srow, erow):
            for j in range(scol, ecol):
                res[i-srow][j-scol] = grid[i][j]
        return res
