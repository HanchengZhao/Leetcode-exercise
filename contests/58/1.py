class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = sum(nums)
        for i, val in enumerate(nums):
            if i > 0:
                left += nums[i-1]
            right -= val
            if left == right:
                return i
        return -1
s = Solution()
print s.pivotIndex([1, 2,3])
