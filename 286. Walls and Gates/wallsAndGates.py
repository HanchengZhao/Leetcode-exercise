from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        
        inf = 2 ** 31 - 1
        r = [0, 0, 1, -1]
        c = [1, -1, 0, 0]
        if not rooms:
            return
        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        for row in xrange(m):
            for col in xrange(n):
                if rooms[row][col] == 0:
                    queue.append((row, col)) # record all gates position
        while queue:
            row, col = queue.popleft()
            for i in xrange(4): # check 4 directions
                n_r = row + r[i] # new row
                n_c = col + c[i] # new col
                if n_r >= 0 and n_r < m and n_c >= 0 and n_c < n:# inside matrix
                    if rooms[n_r][n_c] == inf:
                        rooms[n_r][n_c] = rooms[row][col] + 1
                        queue.append((n_r, n_c))
'''
Start from gate, push visited position to the queue and do the bfs. We do not need to update the
matrix when we reach here from the second gate is because the first reached range will always be 
the smallest
'''