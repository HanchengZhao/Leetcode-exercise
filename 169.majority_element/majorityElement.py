class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # moore voting algorithm
        count = 0
        for i in nums:
            if count == 0:
                major = i
            if i == major:
                count += 1
            else:
                count -= 1
        return major
