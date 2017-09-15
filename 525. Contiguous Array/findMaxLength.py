class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = {0: -1}
        maxLength = 0
        cumulative = 0
        for i, val in enumerate(nums):
            cumulative += 1 if val == 1 else -1
            if cumulative in prefix:
                maxLength = max(maxLength, i-prefix[cumulative])
            else:
                prefix[cumulative] = i
        return maxLength
'''
it basically has the same idea of lc325, use a dictionary 
tor record all prefix sum
'''