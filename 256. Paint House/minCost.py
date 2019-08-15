class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0] * 3
        for red, blue, green in costs:
            next_dp = [0] * 3
            next_dp[0] = min(dp[1] + red, dp[2] + red)
            next_dp[1] = min(dp[0] + blue, dp[2] + blue)
            next_dp[2] = min(dp[0] + green, dp[1] + green)
            dp = next_dp[:]
        return min(dp)


'''
we save all the minimun cost when painting the current house color c,
based on the previous house's minimum cost on a different color
'''
