class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        odds = 0
        evens = 0
        for i in chips:
            if i & 1 == 1:
                odds += 1
            else:
                evens += 1
        return min(odds, evens)
