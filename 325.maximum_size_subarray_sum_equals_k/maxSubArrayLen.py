'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
'''
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # fake entry to make sum consistent
        prefix = {0 : -1} # key is cumulative and value is starting index
        cumulative, longest = 0, 0
        for i, val in enumerate(nums):
            cumulative += val
            if cumulative not in prefix:
                prefix[cumulative] = i #only recording first occurance to make it max
            if cumulative - k in prefix:
                longest = max(longest, i - prefix[cumulative-k])
        return longest

