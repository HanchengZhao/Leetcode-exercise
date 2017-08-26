class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        memo = [[None] * 2001 for i in xrange(len(nums))]
        return self.calculate(nums, S, 0, 0, memo)
    def calculate(self, nums, S, i, sum, memo):
        if i == len(nums): # reach the end
            if sum == S:
                return 1 # sum matched
            else:
                return 0
        else:
            if memo[i][sum]: # already calculated
                return memo[i][sum]
            else: # not calculated
                add = self.calculate(nums, S, i+1, sum+nums[i], memo)
                sub = self.calculate(nums, S, i+1, sum-nums[i], memo)
                memo[i][sum] = add + sub
                return memo[i][sum]
s = Solution()
print s.findTargetSumWays([25,33,27,23,46,16,10,27,33,2,12,2,29,44,49,40,32,46,7,50],4)


