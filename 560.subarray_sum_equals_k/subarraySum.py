class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        count = 0
        prefixSum = [0] * (len(nums)+1)
        prefixSum[0] = 0
        prefixSum[1] = nums[0]
        for i in xrange(2, len(nums)+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
        for i in xrange(len(nums)+1):
            for j in xrange(i+1,len(nums)+1):
                if prefixSum[j] - prefixSum[i] == k:
                    count += 1
        return count
#TLE
s = Solution()
print s.subarraySum([0,0,0,0,0,0,0,0,0,0]
,0)