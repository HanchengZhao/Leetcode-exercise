import bisect

'''
The plain dp will traverse the array in 2 loops, but we can use 
binary search to traverse the array only once to get the answers.

When we reach each number, we only need to know how long is the sequence before 
it that contains numbers smaller than it. So our strategy is:
1. when we meet a number > last element in the sequence:
    - append it to the end
2. new number is smaller than the last element:
    - we find the correct index to update the sequence
The sequence we get is not necessarily the LIS, because we didn't care about the order when updating. 
However, it's guaranteed that its length should be correct, since we know already know there is at least
a sequence of this length before this element.
'''


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
