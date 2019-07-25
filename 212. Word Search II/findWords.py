from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        self.isword = "#"
        Trie = self.buildTrie(words)
        m = len(board)
        n = len(board[0])
        # use set to remove duplicates
        self.res = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in Trie:
                    visited = set()
                    self.dfs(board, i, j, visited, "", Trie)
        return list(self.res)

    def dfs(self, board, i, j, visited, curword, Trie):
        curword += board[i][j]
        Trie = Trie[board[i][j]]
        if self.isword in Trie:
            self.res.add(curword)
        dx = [-1, 0, 0, 1]
        dy = [0, 1, -1, 0]
        visited.add((i, j))
        for n in range(4):
            nx = i + dx[n]
            ny = j + dy[n]
            if 0 <= nx < len(board) and \
               0 <= ny < len(board[0]) and \
               (nx, ny) not in visited and \
               board[nx][ny] in Trie:
                self.dfs(board, nx, ny, visited, curword, Trie)
        visited.remove((i, j))

    def buildTrie(self, words):
        root = {}
        for w in words:
            node = root
            for char in w:
                node = node.setdefault(char, {})
            node[self.isword] = self.isword
        return root


if __name__ == "__main__":
    s = Solution()
    s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                ["oath", "pea", "eat", "rain"])
