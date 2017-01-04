class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.n = len(matrix)
        if self.n == 0:
            return 0
        self.m = len(matrix[0])
        self.dp = [[0]*self.m for i in range(self.n)]
        self.flag = [[0]*self.m for i in range(self.n)]
        ans = 0

        for i in range(self.n):
            for j in range(self.m):
                self.dp[i][j] = self.search(i, j, matrix)
                ans = max(ans, self.dp[i][j])

        return ans

    def search(self,x, y, matrix):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        flag = self.flag
        dp = self.dp
        if(flag[x][y] != 0):
            return dp[x][y]
        ans = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < self.n and 0 <= ny and ny < self.m:
                if matrix[x][y] > matrix[nx][ny]:
                    ans = max(ans, self.search(nx, ny, matrix)+1)

        flag[x][y] = 1
        dp[x][y] = ans
        return ans
