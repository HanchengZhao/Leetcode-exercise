class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, res = 0, 0
        dif = []

        for i in xrange(1,len(prices)):
            dif.append(prices[i] - prices[i-1])

        for i in xrange(len(dif)):
            profit += dif[i]
            if profit < 0:
                profit = 0
            res = max(profit, res)
        return res
