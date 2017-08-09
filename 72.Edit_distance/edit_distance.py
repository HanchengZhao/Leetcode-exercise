class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        row = len(word1)
        col = len(word2)
        dp = [[0] * (col+1) for i in xrange(row+1)]
        for i in xrange(1, col+1):
            dp[0][i] = i
        for i in xrange(1, row+1):
            dp[i][0] = i
        for i in xrange(1, row+1):
            for j in xrange(1, col+1):
                if (word1[i-1] == word2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[row][col]