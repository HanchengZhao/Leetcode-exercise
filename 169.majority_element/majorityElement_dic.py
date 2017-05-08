class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
            if dic[i] > len(nums) / 2:
                return i
