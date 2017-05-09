'''
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.
'''
class Solution(object):
    def findPaths(self, m, n, N, x, y):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dp = [[0] * n for i in xrange(m)]
        dp[x][y] = 1
        count = 0
        for moves in xrange(1, N+1):
            temp = [[0] * n for i in xrange(m)]
            for i in xrange(m):
                for j in xrange(n):
                    if i == m-1:
                        count = (count + dp[i][j]) % mod
                    if j == n-1:
                        count = (count + dp[i][j]) % mod
                    if i == 0:
                        count = (count + dp[i][j]) % mod
                    if j == 0:
                        count = (count + dp[i][j]) % mod
                    temp[i][j] = (((dp[i-1][j] if i>0 else 0) + (dp[i+1][j] if i<m-1 else 0)) % mod + ((dp[i][j-1] if j>0 else 0) +(dp[i][j+1] if j<n-1 else 0))%mod) % mod
            dp = temp
        return count
s = Solution()
print s.findPaths(1,3,3,0,1)