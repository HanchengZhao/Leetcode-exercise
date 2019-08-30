from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        res = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i - k + 1 >= 0:
                res.append(nums[d[0]]) # the leftmost element is always the largest
        return res
'''
Keep indexes of good candidates in deque d. The indexes in d are from the current window, they're increasing, and their corresponding nums are decreasing. Then the first deque element is the index of the largest window value.

For each index i:

Pop (from the end) indexes of smaller elements (they'll be useless).
Append the current index.
Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
If our window has reached size k, append the current window maximum to the output.
'''