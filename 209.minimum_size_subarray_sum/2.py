class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = float('inf')
        start = 0
        Sum = 0
        for i in xrange(len(nums)):
            Sum += nums[i]
            while Sum >= s and start <= i:
                res = min(res, i-start+1)
                Sum -= nums[start]
                start += 1
        if res == float('inf'):
            return 0
        else:
            return res
                
                