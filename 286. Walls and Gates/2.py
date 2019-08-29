class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        queue = []
        inf = 2147483647
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
        x = [-1, 0, 0, 1]
        y = [0, 1, -1, 0]
        visited = set()
        while queue:
            nxt = queue.pop(0)
            visited.add((nxt[0], nxt[1]))
            for i in range(4):
                nx = i + nxt[0]
                ny = j + nxt[1]
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and rooms[nx][ny] == inf:
                    rooms[nx][ny] = nxt[2] + 1
                    queue.append((nx, ny, nxt[2]+1))
