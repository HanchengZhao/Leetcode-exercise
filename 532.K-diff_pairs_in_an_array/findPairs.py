class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2 or k < 0:
        	return 0
        nums.sort()
        seenNum = set()
        seenPair = set()
        count = 0
        for i in xrange(len(nums)):
        	prev = nums[i] - k
        	if prev in seenNum and (prev, nums[i]) not in seenPair:
        		count += 1
        		seenPair.add((prev, nums[i]))
        	seenNum.add(nums[i])
        return count