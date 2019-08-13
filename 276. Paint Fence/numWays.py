class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return k ** n
        # same, diff
        dp = [[0, 0] for i in range(n)]
        dp[0] = [0, k]
        dp[1] = [k, k * (k-1)]

        for i in range(2, n):
            # same as previous one, then pre should be diff than pre2
            dp[i][0] = dp[i-1][1]
            # diff than prev,
            dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * (k-1)
        return dp[-1][0] + dp[-1][1]
