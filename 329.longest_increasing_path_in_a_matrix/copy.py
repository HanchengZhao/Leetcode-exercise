class Solution:
    DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return 0

        self.n = len(A)
        self.m = len(A[0])
        self.matrix = [[0] * self.m for i in xrange(self.n)]

        for i in xrange(self.n):
            for j in xrange(self.m):
                self.search(A, i, j)

        return max(max(row) for row in self.matrix)

    def search(self, A, x, y):
        if self.matrix[x][y] != 0:
            return self.matrix[x][y]

        longest = 1
        for dx, dy in self.DIRECTIONS:
            if x + dx < 0 or x + dx >= self.n:
                continue
            if y + dy < 0 or y + dy >= self.m:
                continue
            if A[x][y] >= A[x + dx][y + dy]:
                continue
            longest = max(longest, self.search(A, x + dx, y + dy) + 1)
        self.matrix[x][y] = longest
        return self.matrix[x][y]