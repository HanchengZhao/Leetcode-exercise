# http://www.geeksforgeeks.org/longest-common-substring/
def longestCommonSubstring(x, y, m, n):
    # m is length of x,
    # n is length of y
    dp = [[0] * (n+1) for i in xrange(m+1)]
    res = 0
    for i in xrange(m):
        for j in xrange(n):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                res = max(res, dp[i+1][j+1])
    return res

print longestCommonSubstring('GeeksforGeeks', 'GeeksQuiz',13,9)