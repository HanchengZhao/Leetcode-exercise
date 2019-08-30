class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[float("inf")]*n for _ in range(m+1)]
        Sums = [0] * (n + 1)
        for i in range(n):
            Sums[i+1] = Sums[i] + nums[i]
        for i in range(n):
            dp[1][i] = Sums[i+1]
        for i in range(2, m+1):
            for j in range(i-1, n):
                for k in range(j):
                    dp[i][j] = min(dp[i][j], max(
                        dp[i-1][k], Sums[j+1] - Sums[k+1]))
        return dp[m][n-1]
'''
dp solution

time: O(mn^2)
'''
