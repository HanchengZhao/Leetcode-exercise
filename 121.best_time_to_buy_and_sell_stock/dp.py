class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        smallest = prices[0] # record the previous smallest price
        dp = [0] * len(prices)
        for i in xrange(1, len(prices)):
            dp[i] = max(prices[i] - smallest, dp[i-1])
            smallest = min(smallest, prices[i])
        return dp[-1]