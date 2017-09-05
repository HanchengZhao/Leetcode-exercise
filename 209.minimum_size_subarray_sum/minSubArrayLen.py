import sys

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        Sum = 0
        res = sys.maxint
        for i in range(len(nums)):
            while j < len(nums) and Sum < s:
                Sum += nums[j]
                j += 1
            if Sum >= s: #the while loop can be ended when j > len(nums)
                res = min(res, j - i) #record minimum length, j has been added 1, so it is not j-i+1
            Sum -= nums[i]
        if res == sys.maxint:#no match
            return 0
        return res
s = Solution()
print s.minSubArrayLen(7, [2,3,1,2,4,3])