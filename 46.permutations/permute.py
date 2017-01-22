class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = []
        self.helper(nums, ans, temp)
        return ans

    def helper(self, nums, ans, temp):
        if len(nums) == 0:
            ans.append(temp)
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:], ans, temp+[nums[i]])


s = Solution()
print s.permute([1,2,3])