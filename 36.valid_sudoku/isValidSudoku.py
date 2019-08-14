class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subbox = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                val = board[i][j]
                # check rows
                if val in rows[i]:
                    return False
                rows[i].add(val)
                # check cols
                if val in cols[j]:
                    return False
                cols[j].add(val)
                # check sub boxes
                if val in subbox[i//3][j//3]:
                    return False
                subbox[i//3][j//3].add(val)
        return True
