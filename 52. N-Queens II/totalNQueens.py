class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.cols = set()
        self.diag = set()
        self.rev_diag = set()
        self.n = n
        self.dfs(0)
        return self.count

    def dfs(self, row):
        if row == self.n:
            self.count += 1
            return
        for col in range(self.n):
            # will get killed
            if col in self.cols or row - col in self.diag or row + col in self.rev_diag:
                continue
            self.cols.add(col)
            self.diag.add(row - col)
            self.rev_diag.add(row + col)

            self.dfs(row + 1)

            self.cols.remove(col)
            self.diag.remove(row-col)
            self.rev_diag.remove(row + col)

# time : O(N!), cause there are N ways to put the first one, and N-2 for the second one


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))
