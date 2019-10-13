from collections import deque
def minimumDistance(numRows, numColumns, area):
    if area[0][0] != 1:
        return -1
    queue = deque([[(0,0), 0]])
    visited = set()
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    while queue:
        pos, dist = queue.popleft()
        print(pos, dist)
        visited.add(pos)
        for dir in directions:
            print(pos, dir)
            nx = pos[0] + dir[0]
            ny = pos[1] + dir[1]
            if 0 <= nx < numRows and 0 <= ny < numColumns \
                and (nx, ny) not in visited:
                if area[nx][ny] == 9:
                    return dist + 1 
                if area[nx][ny] == 1:
                    queue.append([(nx, ny), dist + 1])
    return -1
print(minimumDistance(3, 3, [[1, 0, 0], [1, 0, 0], [1, 9, 1]]))