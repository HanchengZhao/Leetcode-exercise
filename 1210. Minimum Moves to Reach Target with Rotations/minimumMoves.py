class Solution:
    def minimumMoves(self, grid) -> int:
        n = len(grid)
        start = (0, 0, 0, 1)
        end = (n-1, n-2, n-1, n-1)
        visited = set()
        step = 0
        # use {} to make (0,0,0,1) as an iterable, otherwise, it iterates through each digit
        cur_level = {start}
        while cur_level:
            next_level = set()
            for pos in cur_level:
                visited.add(pos)
                r1, c1, r2, c2 = pos
                # to right:
                if c1 + 1 < n and grid[r1][c1+1] == 0 and c2 + 1 < n and grid[r2][c2+1] == 0:
                    if (r1, c1 + 1, r2, c2 + 1) not in visited:
                        next_level.add((r1, c1 + 1, r2, c2 + 1))
                # down
                if r1 + 1 < n and grid[r1+1][c1] == 0 and r2 + 1 < n and grid[r2+1][c2] == 0:
                    if (r1 + 1, c1, r2 + 1, c1) not in visited:
                        next_level.add((r1 + 1, c1, r2 + 1, c2))
                # rotate, from horizontal to vertical
                if r1 == r2 and r1 + 1 < n and grid[r1+1][c1] + grid[r1+1][c1+1] == 0:
                    if (r1, c1, r1 + 1, c1) not in visited:
                        next_level.add((r1, c1, r1 + 1, c1))
                # rotate, from vertical to horizontal
                if c1 == c2 and r2 == r1 + 1 and c1 + 1 < n and grid[r1][c1+1] + grid[r1+1][c1+1] == 0:
                    if (r1, c1, r1, c1 + 1) not in visited:
                        next_level.add((r1, c1, r1, c1 + 1))
            if end in next_level:
                return step + 1
            step += 1
            cur_level = next_level
        return -1
