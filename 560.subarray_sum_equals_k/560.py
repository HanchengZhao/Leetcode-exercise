class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        stored = []
        count = 0
        for i in xrange(len(nums)):
            stored = list(map(lambda x: x + nums[i], stored))
            stored.append(nums[i])
            if k in stored:
                count += stored.count(k)
        return count
s = Solution()
print s.subarraySum([0,0,0,0,0,0,0,0,0,0]
,0)