class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i, m in enumerate(nums):
            remain = nums[:i] + nums[i+1:]
            for arr in self.permute(remain):
                res.append([m] + arr)
        return res
