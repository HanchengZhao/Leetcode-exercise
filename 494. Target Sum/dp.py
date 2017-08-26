class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        if nums[0] == 0:
            dic = {0:2} # +0 and -0
        else:
            dic = {nums[0]:1, -nums[0]:1}
        for i in xrange(1, len(nums)):
            nextdic = {}
            for key in dic:
                nextdic[key + nums[i]] = nextdic.get(key + nums[i], 0) + dic[key] # calculated + # of steps to get here
                nextdic[key - nums[i]] = nextdic.get(key - nums[i], 0) + dic[key]
            dic = nextdic # update
        return dic.get(S, 0)
'''
update dic every time and save all the overlapped result in the same key for next use
time : O(n^2)
space : O(n^2)
'''