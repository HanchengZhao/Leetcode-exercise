class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums)-2):
            if i == 0 or i != 0 and nums[i] != nums[i-1]: # remove duplicate first element
                target = 0 - nums[i]
                lo = i+1
                hi = len(nums) - 1
                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo + 1] == nums[lo]:  # avoid duplicate elements
                            lo += 1
                        while lo < hi and nums[hi - 1] == nums[hi]:
                            hi -= 1
                        # do not forget to update index
                        lo += 1 
                        hi -= 1
                    elif nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        hi -= 1
        return res
s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])
            