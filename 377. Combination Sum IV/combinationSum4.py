class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        d = {0 : 1} # map to store used target
        return self.helper(nums, target, d)

    def helper(self, nums, target, d):
        if target in d: # if existed, no need to do it agian
            return d[target]
        res = 0
        for i in nums:
            if target >= i:
                res += self.helper(nums, target - i, d)
        d[target] = res
        return res
s = Solution()
print s.combinationSum4([1,2,3], 4)

'''
if target has only one number left to reach, so loop through the nums to check the state:
in this example, comb(4) = comb(4-1) + comb(4-2) +comb(4-3)
since comb(0) = 1, we can store that in a map and start dp. 

follow up:
The problem with negative numbers is that now the combinations could be potentially of infinite length. 
Think about nums = [-1, 1] and target = 1. We can have all sequences of arbitrary length that follow the patterns
 -1, 1, -1, 1, ..., -1, 1, 1 and 1, -1, 1, -1, ..., 1, -1, 1 (there are also others, of course, just to give an example). 
 So we should limit the length of the combination sequence, so as to give a bound to the problem.
'''
