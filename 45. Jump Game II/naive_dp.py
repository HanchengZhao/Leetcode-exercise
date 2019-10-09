class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf") for i in range(n)]
        dp[0] = 0
        for i, val in enumerate(nums):
            for j in range(1, min(n, val + i + 1)):
                dp[j] = min(dp[i]+1, dp[j])
        return dp[-1]


'''
TLE
'''
