class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for i in xrange(m+1)]
        dp[0][0] = True
        # initialize the first row
        for i in xrange(n):
            if p[i] == "*" and dp[0][i-1]:
                dp[0][i+1] = True
        for i in xrange(m):
            for j in xrange(n):
                if p[j] == "." or p[j] == s[i]: #match for a certain char
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == "*":
                    if p[j-1] != s[i] and p[j-1] != ".": #empty repeat
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else: #one or more repeat
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]
        return dp[m][n]