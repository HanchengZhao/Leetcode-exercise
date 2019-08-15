class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_take, prev_nottake = 0, 0
        for i in nums:
            prev_take, prev_nottake = prev_nottake + \
                i, max(prev_take, prev_nottake)
        return max(prev_take, prev_nottake)


'''
record the maximum gain based on whether robbing the current house or not
'''
