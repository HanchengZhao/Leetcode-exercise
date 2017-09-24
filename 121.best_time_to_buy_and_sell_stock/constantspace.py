class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smallest = float('inf')
        res = 0
        for i in prices:
            if i < smallest:
                smallest = i
            res = max(res, i - smallest)
        return res