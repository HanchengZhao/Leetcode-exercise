import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        LIS = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] < LIS[-1]:
                index = bisect.bisect_left(LIS, nums[i])
                LIS[index] = nums[i]
            elif nums[i] > LIS[-1]:
                LIS.append(nums[i])
        return len(LIS)
