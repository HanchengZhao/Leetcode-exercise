
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = A[0][:]
        n = len(A)
        m = len(A[0])
        for i in range(1, n):
            dp2 = [0] * m
            for j in range(m):
                dp2[j] = min(dp[j-1] if j > 0 else float("inf"), dp[j],
                             dp[j+1] if j < m - 1 else float("inf")) + A[i][j]
            dp = dp2
        return min(dp)
