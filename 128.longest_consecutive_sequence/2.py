class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        for i in nums:
            if i not in dic: # only check for unvisited nums
                left = dic.get(i-1, 0)
                right = dic.get(i+1, 0)
                length = left + right + 1
                res = max(length, res)
                dic[i] = length
                # only need update border because we only check unvisited nums
                dic[i-left] = length # left border
                dic[i+right] = length # right border
        return res
'''
use a dictionary to track length up to current digit, and update left and right border 
every time
'''