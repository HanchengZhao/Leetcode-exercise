class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # since the requirement is inplace, we can not use a
        # separate array to store the count
        # but we can use a new encoding way to represent 4 state:
        # 0 : "dead", 1:"live", 2:"dead -> live", 3: "live->dead"
        m,n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                #current dead
                if board[i][j] == 0 or board[i][j] == 2:
                    if self.countLife(board,i,j) == 3:
                        board[i][j] = 2 #back to life
                else:
                    if self.countLife(board,i,j) < 2 or self.countLife(board,i,j) > 3:
                        board[i][j] = 3
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0
    def countLife(self, board, i, j):
        m,n = len(board), len(board[0])
        count = 0
        if i-1 >= 0 and j-1 >= 0 :  count += board[i-1][j-1]%2
        if i-1 >=0:                 count += board[i-1][j]%2
        if i-1 >= 0 and j+1 < n :  count += board[i-1][j+1]%2
        if j-1 >= 0:                count += board[i][j-1]%2
        if j+1 < n:                count += board[i][j+1]%2
        if i+1 < m and j-1 >= 0 :  count += board[i+1][j-1]%2
        if i+1 < m:                count += board[i+1][j]%2
        if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2
        return count