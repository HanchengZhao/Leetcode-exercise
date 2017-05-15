class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in xrange(1, len(nums)):
            longest = 1
            for j in xrange(0,i):
                if nums[i] > nums[j]:
                    longest = max(dp[j] + 1, longest)
            dp[i] = longest
        return max(dp)

