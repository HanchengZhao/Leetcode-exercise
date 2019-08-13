class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if len(grid) <= 1:
            return 0
        row, col = len(grid), len(grid[0])
        memo = {}
        for r in grid:
            for i in range(col-1):
                for j in range(i+1, col):
                    if r[i] and r[j]:
                        memo[(i, j)] = memo.get((i, j), 0) + 1
        res = 0
        for v in memo.values():
            # combinations
            res += v * (v-1) // 2
        return res


'''
time: O(row * col ^2)
use memo to record the each line, then calculate the combinations in the end
'''
