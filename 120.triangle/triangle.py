# traverse from bottom up,
# dp[i][j] means the minimum path from the bottom to this node


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = [[0] * len(triangle) for i in range(len(triangle))]
        # init last row
        for i, val in enumerate(triangle[-1]):
            dp[-1][i] = val
        for i in range(len(dp)-2, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]
