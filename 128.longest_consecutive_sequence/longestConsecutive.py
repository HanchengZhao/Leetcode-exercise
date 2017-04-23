class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        for i in nums:
            if not dic.has_key(i):
                left = dic[i-1] if dic.has_key(i-1) else 0
                right = dic[i+1] if dic.has_key(i+1) else 0
                length = left + right + 1
                dic[i] = length
                res = max(res, length)
                dic[i-left] = length
                dic[i+right] = length
        return res