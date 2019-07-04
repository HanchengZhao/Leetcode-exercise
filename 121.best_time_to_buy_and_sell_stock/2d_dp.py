class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0] * 2 for i in range(len(prices))]  # max profit
        dp[0][0] = 0  # profit when holidng 0 stock
        dp[0][1] = -prices[0]  # buy the first stock
        for i in range(1, len(prices)):
            # max of (selling the stock, the same as the day before)
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            # can only sell once
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[-1][0]
