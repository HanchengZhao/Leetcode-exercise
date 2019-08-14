class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # find first increace element from end
        inc = -1
        for i in xrange(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]:
                inc = i-1
                break
        nextsmaller = 0
        if inc == -1:  # increasing array
            return nums[::-1]

        for i in xrange(len(nums)-1, inc, -1):
            if nums[i] < nums[inc]:
                nextsmaller = i
        # swap
        nums[inc], nums[nextsmaller] = nums[nextsmaller], nums[inc]
        # reverse
        rev = nums[inc:]
        for i in xrange(len(nums)-1 - inc):
            nums[len(nums)-1-inc + i] = rev[i]
        return nums
s = Solution()
print s.previousPermuation([1,2,3,4])