class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        # rob the first one
        dp = [[0, 0] for i in range(len(nums))]
        for i in range(2, len(nums)-1):
            # skip this house
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            # rob this house
            dp[i][1] = dp[i-1][0] + nums[i]

        rob_first = nums[0] + max(dp[-2][0], dp[-2][1])
        # don't rob the first
        dp = [[0, 0] for i in range(len(nums))]
        for i in range(1, len(nums)):
            # skip this house
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            # rob this house
            dp[i][1] = dp[i-1][0] + nums[i]
        not_rob_first = max(dp[-1][0], dp[-1][1])
        return max(rob_first, not_rob_first)


'''
use dp to record 2 cases:
    - rob the first house
          - skip the last
    - don't rob the first 
          - skip the first
'''
