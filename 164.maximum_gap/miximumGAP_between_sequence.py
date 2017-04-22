class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        maxdif = 0
        increment = 1
        startPos = 0
        for i in xrange(1, len(nums)):
            dif = nums[i] - nums[i-1]
            if dif * increment < 0: # change start pos
                increment *= -1
                startPos = i-1
            maxdif = max(maxdif, abs(nums[i] - nums[startPos]))
        return maxdif
s = Solution()
print s.maximumGap([1,2,3,4,5,6,5,2,4,9])