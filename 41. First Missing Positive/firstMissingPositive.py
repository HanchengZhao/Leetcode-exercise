# Your algorithm should run in O(n) time and uses constant extra space.
# we are required to use constant extra space, so we have to utilize the input array we already have

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # check if 1 is in the array
        if not nums or 1 not in nums:
            return 1
        # clean data, replace all negative ints and numbers that are > len(List) with 1s
        # we already make sure that there is no 1 here
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        # mark the existence of all positive numbers with the negative sign
        for i in range(len(nums)):
            new_index = abs(nums[i])
            if new_index == n:
                nums[0] = - abs(nums[0])
            else:
                nums[new_index] = - abs(nums[new_index])
        # loop through array, return the first missing positive
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1


s = Solution()
print(s.firstMissingPositive([1, 2, 0]))
