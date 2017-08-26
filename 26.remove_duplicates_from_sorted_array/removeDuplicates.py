class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        i = 1
        for j in xrange(1, n):
            if nums[j] != nums[j-1]: # no duplicate
                nums[i] = nums[j]
                i += 1
        return i # nums after i are duplicates
'''
move none duplicates forward
'''