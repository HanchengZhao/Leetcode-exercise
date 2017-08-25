import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result = -1
        count = 0
        for i in xrange(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, count) == 0: # chance of 1/count
                    result = i #it will gaurantee that the first occurrence will be selected since randint(0, 0) = 0
                count += 1
        return result
        
'''
reservoir sampling

Consider the example in the OJ
{1,2,3,3,3} with target 3, you want to select 2,3,4 with a probability of 1/3 each.

2 : It's probability of selection is 1 * (1/2) * (2/3) = 1/3
3 : It's probability of selection is (1/2) * (2/3) = 1/3
4 : It's probability of selection is just 1/3

So they are each randomly selected.
'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# https://www.youtube.com/watch?v=s_Za9GlD0ek