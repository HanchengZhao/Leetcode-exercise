from collections import defaultdict
import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.index = defaultdict(list)
        for i, val in enumerate(nums):
            self.index[val].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indexList = self.index[target]
        return indexList[random.randint(0, len(indexList)-1)]
        
'''
dictionary here will cause memory limit exceeded
'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)