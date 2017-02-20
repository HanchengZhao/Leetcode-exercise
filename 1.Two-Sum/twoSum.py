class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [i,dic[nums[i]]]
            else:
                compliment = target - nums[i]
                dic[compliment] = i
