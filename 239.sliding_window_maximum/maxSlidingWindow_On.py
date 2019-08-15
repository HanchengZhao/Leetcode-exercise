from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # edge case
        if not nums:
            return []
        # record the largest index
        window = deque()
        res = []
        for i, val in enumerate(nums):
            if i >= k and window[0] <= i-k:
                window.popleft()
            while window and val >= nums[window[-1]]:
                window.pop()

            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res
