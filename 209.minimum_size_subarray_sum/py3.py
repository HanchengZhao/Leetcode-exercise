class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float("inf")
        j = -1
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                res = min(res, i - j)
                j += 1
                Sum -= nums[j]
        return res if res != float("inf") else 0
