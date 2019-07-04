# use dp to record days, transactions and stock status
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[[0] * 2 for i in range(3)]for i in range(len(prices))]
        # i, j, k means days, transactions, whether has stock
        dp[0][0][0], dp[0][0][1] = 0, - prices[0]
        dp[0][1][0], dp[0][1][1] = float("-inf"), float("-inf")
        dp[0][2][0], dp[0][2][1] = float("-inf"), float("-inf")

        for i in range(1, len(prices)):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])

            dp[i][1][0] = max(dp[i-1][0][1] + prices[i], dp[i-1][1][0])
            dp[i][1][1] = max(dp[i-1][1][0] - prices[i], dp[i-1][1][1])

            dp[i][2][0] = max(dp[i-1][1][1] + prices[i], dp[i-1][2][0])
        return max(dp[-1][0][0], dp[-1][1][0], dp[-1][2][0])
