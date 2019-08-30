class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]: # if number is bigger than past 2 nums before i
                nums[i] = n
                i += 1
        return i
'''
almost same idea as 19, but compare one more number.abs
Just go through the numbers and include those in the result that haven't been included twice already.
'''