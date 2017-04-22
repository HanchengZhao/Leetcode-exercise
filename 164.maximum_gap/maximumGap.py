class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #bucket sort
        if len(nums) < 2:
            return 0
        # find the range
        Min = float("inf")
        Max = float("-inf")
        maxgap = 0
        for i in nums:
            Min = min(i, Min)
            Max = max(i, Max)
        bucket = [0 * x for x in range(Min, Max+1)]
        #bucket sort
        for j in nums:
            if not bucket[j-Min]:
                bucket[j-Min] = 1
        #find largest gap
        print bucket
        prev = 0
        for k in xrange(len(bucket)):
            if bucket[k]:
                maxgap = max(maxgap, k-prev)
                prev = k
        return maxgap
#Tle
s = Solution()
print s.maximumGap([1,2,3,4,5,6,5,2,4,9])