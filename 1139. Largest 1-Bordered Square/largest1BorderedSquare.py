class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        Max = 0
        # create 2 auxillary array to save horizontal and vertial prefix sum
        hon = [[0] * n for _ in range(m)]
        ver = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hon[i][j] = hon[i][j-1] + 1 if j > 0 else 1
                    ver[i][j] = ver[i-1][j] + 1 if i > 0 else 1
        # start from the bottom right
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                small = min(hon[i][j], ver[i][j])
                # check for each possible length, get the
                while small > Max:
                    # check for each line
                    if hon[i-small+1][j] >= small and ver[i][j-small+1] >= small:
                        Max = max(Max, small)
                    small -= 1
        return Max * Max
