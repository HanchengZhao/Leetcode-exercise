class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        insertIndex = 0
        for i in nums:
            if i:
                nums[insertIndex] = i
                insertIndex += 1
        for j in xrange(insertIndex, len(nums)):
            nums[j] = 0
