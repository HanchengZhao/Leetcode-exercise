class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.solve(board)
    def solve(self, board):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '.':
                    for c in xrange(1, 10):
                        if self.isValid(board, i, j, str(c)):
                            board[i][j] = str(c) # put c for this cell
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.' # else go back
                    return False
        return True
    def isValid(self, board, row, col, c):
        for i in xrange(9):
            if board[i][col] != '.' and board[i][col] == c: # check row
                return False
            if board[row][i] != '.' and board[row][i] == c: # check column
                return False
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] != '.' and 
            board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c): # check 3*3 block
                return False
        return True