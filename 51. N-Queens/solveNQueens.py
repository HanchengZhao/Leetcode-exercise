class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diags = set()
        rev_diags = set()

        def dfs(cur, row):
            if row >= n:
                res.append(cur)
                return
            for col in range(n):
                # get killed
                if col in cols or row - col in diags or row + col in rev_diags:
                    continue
                cols.add(col)
                # postions on the same diagnol line will have the same (x - y)
                diags.add(row - col)
                # (x+y) would equal to a constant if they are on the same reverse diagnal line
                rev_diags.add(row + col)

                dfs(cur + [col], row + 1)
                # recover
                cols.remove(col)
                diags.remove(row - col)
                rev_diags.remove(row + col)
        dfs([], 0)
        return self._generate(res, n)

    def _generate(self, res, n):
        boards = []
        for r in res:
            board = []
            for col in r:
                s = ""
                for i in range(n):
                    s += "Q" if i == col else "."
                board.append(s)
            boards.append(board)
        return boards
