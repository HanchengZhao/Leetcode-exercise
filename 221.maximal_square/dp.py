class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+1) for i in xrange(m+1)] # initialize with 1 more length to contain every elements
        maxlen = 0
        for i in xrange(1, m+1): # m+1 not m
            for j in xrange(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    maxlen = max(maxlen, dp[i][j])
        return maxlen * maxlen
'''
check if previous diagonal string is 1, then save min(previous neigbours) + 1
'''
s = Solution()
print s.maximalSquare([["1"]])