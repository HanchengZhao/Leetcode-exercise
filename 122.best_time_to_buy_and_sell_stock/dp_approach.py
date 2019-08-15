# we can also use dp approach to solve it
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0] * 2 for i in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = - prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]
