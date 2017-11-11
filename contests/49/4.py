class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        cnt = [(1,1)] * len(nums) # (length, count)
        for i in xrange(1, len(nums)):
            Max = 1
            count = 1
            for j in xrange(i):
                if nums[i] > nums[j]:
                    # Max = max(Max, dp[j]+1)
                    if dp[j]+1 > Max:
                        Max = dp[j]+1
                        count = cnt[j][1]
                    elif dp[j]+1 == Max:
                        count += cnt[j][1]
            dp[i] = Max
            cnt[i] = (Max, count)
        longest = max(dp)
        number = 0
        for i in cnt:
            if i[0] == longest:
                number += i[1]
        return number
s =Solution()
print s.findNumberOfLIS([1,3,5,4,7])
print s.findNumberOfLIS([2,2,2,2,2])
print s.findNumberOfLIS([1,2,4,3,5,4,7,2])
# 3