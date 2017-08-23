class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # loop through the grid, find the char that matches the first char of word, then
        # dfs its neighbors to find the next char
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if self.dfs(i, j, board, word, visited):
                    return True
        return False

    def dfs(self, i, j, board, word, visited):
        if len(word) == 0: # found all chars on board
            return True
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or 
        visited[i][j] or board[i][j] != word[0]): # out of bound or visited or not equal
            return False
        visited[i][j] = True # match the char
        res = (self.dfs(i+1, j, board, word[1:], visited)  # check 4 directions
            or self.dfs(i, j+1, board, word[1:], visited) 
            or self.dfs(i-1, j, board, word[1:], visited) 
            or self.dfs(i, j-1, board, word[1:], visited))
        visited[i][j] = False # recover for next round dfs
        return res


