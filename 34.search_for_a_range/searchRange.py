class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            if nums[lo] == target and nums[hi] == target:
                return [lo, hi]
            if nums[lo] < target:
                lo += 1
            if nums[hi] > target:
                hi -= 1
        return [-1, -1]
