class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        longest = 1
        cur = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
                longest = max(longest, cur)
            else:
                cur = 1
        return longest
s = Solution()
print s.findLengthOfLCIS([1,3,5,7])