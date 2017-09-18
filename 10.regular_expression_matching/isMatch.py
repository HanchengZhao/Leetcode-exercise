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
        # initialize the first row, 'x*' could be empty
        for i in xrange(n): 
            if p[i] == "*" and dp[0][i-1]:
                dp[0][i+1] = True
        for i in xrange(m):
            for j in xrange(n):
                if p[j] == "." or p[j] == s[i]: #match for a certain char
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == "*":
                    if p[j-1] != s[i] and p[j-1] != ".": #can only be empty repeat
                        dp[i+1][j+1] = dp[i+1][j-1] # skip one char back to look up
                    else: #one or more repeat or zero
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]
        return dp[m][n]

'''
1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
3, If p.charAt(j) == '*': 
   here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
'''