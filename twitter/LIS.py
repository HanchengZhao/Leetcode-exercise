class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        maxlen = 1
        for i in xrange(1, len(nums)):
            longest = 1
            for j in xrange(0, i):
                if nums[i] > nums[j]:
                    longest = dp[j] + 1
                    dp[i] = max(dp[i], longest)
                    maxlen = max(maxlen, dp[i])
        return maxlen
'''
TIME O(n^2)
'''