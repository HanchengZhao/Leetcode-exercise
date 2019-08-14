class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True

        def bfs(i, j, word, board, visited):
            if word == "":
                return True
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < len(board) and \
                    0 <= ny < len(board[0]) and \
                    (nx, ny) not in visited and \
                        board[nx][ny] == word[0]:
                    visited.add((nx, ny))
                    if bfs(nx, ny, word[1:], board, visited):
                        return True
                    # this step is import to recover the visited set
                    visited.remove((nx, ny))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if bfs(i, j, word[1:], board, visited):
                        return True
        return False
