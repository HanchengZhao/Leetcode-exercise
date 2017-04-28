class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        s0: able to buy stock
        s1: holding stock
        s2: just sold stock
        """
        n = len(prices)
        if n < 2:
            return 0
        s0, s1, s2 = [0] * n, [0] * n, [0] * n
        s0[0], s1[0], s2[0] = 0, -prices[0], 0
        for i in xrange(1, n):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s0[i - 1] - prices[i], s1[i - 1])
            s2[i] = s1[i - 1] + prices[i]
        return max(s0[n-1], s2[n-1])
