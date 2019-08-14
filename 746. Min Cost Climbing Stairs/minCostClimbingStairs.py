class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        if len(cost) == 2:
            return min(cost)
        dp = [0] * len(cost)
        dp[-1], dp[-2] = cost[-1], cost[-2]
        for i in range(len(cost)-3, -1, -1):
            dp[i] = min(dp[i+1] + cost[i], dp[i+2] + cost[i])
        return min(dp[0], dp[1])


'''
start from the end, check the next 2 cost each time, record the minimum
cost from here to the end
'''
