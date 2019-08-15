class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a, b = text1, text2
        m, n = len(a), len(b)
        dp = [[0] * n for i in range(m)]
        # initialize 1st row
        for i in range(n):
            if a[0] == b[i]:
                dp[0][i] = 1
            elif i != 0:
                dp[0][i] = dp[0][i-1]
        # init 1st col
        for i in range(m):
            if a[i] == b[0]:
                dp[i][0] = 1
            elif i != 0:
                dp[i][0] = dp[i-1][0]
        # traverse the table
        for i in range(1, m):
            for j in range(1, n):
                if a[i] == b[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]

# common dp solution
# use a state transition table to record current longest common sequence length
