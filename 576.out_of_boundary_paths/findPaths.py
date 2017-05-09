'''
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.
'''
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        memo = [[[-1] * (N+1) for i in xrange(n)] for j in xrange(m)]
        return self.recursion(m, n, N, i, j, memo)

    def recursion(self, m, n, N, i, j, memo):
        mod = 10 ** 9 + 7
        if i == m or j == n or i < 0 or j < 0:
            return 1
        if N == 0:
            return 0
        print memo, i, j, N
        if memo[i][j][N] >= 0:
            return memo[i][j][N]
        memo[i][j][N] = self.recursion(m, n, N-1, i-1, j, memo) + self.recursion(m, n, N-1, i+1, j, memo) + self.recursion(m, n, N-1, i, j-1, memo) + self.recursion(m, n, N-1, i, j+1, memo)
        return memo[i][j][N] % mod

s = Solution()
print s.findPaths(1,3,3,0,1)