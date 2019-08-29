#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#


class Solution:
    def PredictTheWinner(self, nums) -> bool:
        n = len(nums)
        memo = [[0 for _ in range(n)] for _ in range(n)]
        prefix = [0 for _ in range(n+1)]
        for i in range(n):
            prefix[i+1] = nums[i] + prefix[i]
        # i, j indicates the start and end
        # recursion also returns the max value

        def subsum(i, j):
            return prefix[j+1] - prefix[i]

        def recursion(nums, i, j, memo):
            if memo[i][j]:
                return memo[i][j]
            if i > j:
                return 0
            if i == j:
                return nums[i]
            if i == j - 1:
                memo[i][j] = max(nums[i], nums[j])
                return memo[i][j]
            # either get first or the last
            memo[i][j] = max(subsum(i+1, j) -
                             recursion(nums, i+1, j, memo) + nums[i],
                             subsum(i, j-1) - recursion(nums, i, j-1, memo) + nums[j])
            return memo[i][j]
        total = prefix[n]
        first_max = recursion(nums, 0, n-1, memo)
        return first_max >= total - first_max


# s = Solution()
# s.PredictTheWinner([1, 5, 233, 7])
