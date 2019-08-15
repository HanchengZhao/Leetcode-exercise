class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i, val in enumerate(nums):
            while stack and stack[-1][0] < val:
                lastval, lastindex = stack.pop()
                res[lastindex] = val
            stack.append((val, i))
        # loop again to find the bigger number for the rest elements in the stack
        for i, val in enumerate(nums):
            while stack and stack[-1][0] < val:
                lastval, lastindex = stack.pop()
                res[lastindex] = val
        return res
