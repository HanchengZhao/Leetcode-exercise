class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        # the problem will become a greedy problem if k is larger than the half length
        if k > len(prices) / 2:
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res

        dp = [[[float("-inf")] * 2 for i in range(k+1)]
              for i in range(len(prices))]
        # init
        for kk in range(k+1):
            # holds 0 stock after numerous transactions
            dp[0][kk][0] = 0
            # holds 1 stock after numerous transactions
            dp[0][kk][1] = - prices[0]

        for i in range(1, len(prices)):
            for kk in range(k+1):
                # need to handle the special case when kk == 0
                dp[i][kk][0] = max(dp[i-1][kk][0], dp[i-1][kk-1]
                                   [1] + prices[i]) if kk > 0 else dp[i-1][kk][0]
                dp[i][kk][1] = max(dp[i-1][kk][0] - prices[i], dp[i-1][kk][1])
        return max([dp[-1][kk][0] for kk in range(k+1)])
