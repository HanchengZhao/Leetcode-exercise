class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)