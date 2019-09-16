class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])
        res = []
        for i, val in enumerate(nums):
            if val > 0:
                res.append(i+1)
        return res


'''
time: O(n)
no extra space
'''
