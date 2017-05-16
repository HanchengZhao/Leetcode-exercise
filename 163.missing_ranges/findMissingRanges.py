class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            return [str(lower)] if lower == upper else [str(lower) + "->" + str(upper)]
        res = []
        for i, v in enumerate(nums):
            if i == 0 and v > lower:
                if v == lower+1: #exactly one
                    res.append(str(lower))
                else:
                    res.append(str(lower) + "->" + str(v - 1))
            elif v - nums[i-1] > 1:
                if v - nums[i-1] == 2:
                    res.append(str(nums[i-1] + 1))
                else:
                    res.append(str(nums[i-1] + 1) + "->" + str(v - 1))
            if i == len(nums) - 1 and v < upper:
                if upper - v == 1:
                    res.append(str(upper))
                else:
                    res.append(str(v+1) + "->" + str(upper))
        return res
s = Solution()
print s.findMissingRanges([0,1,3,50,75,98,99],0,99)
print s.findMissingRanges([],0,123)