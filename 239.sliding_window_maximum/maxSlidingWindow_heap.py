from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        window = deque(nums[:k])
        res = []
        res.append(max(window))
        for i in xrange(k,len(nums)):
            window.append(nums[i])
            window.popleft()
            res.append(max(window))
        return res
# this is a brute force O(n^2) solution, there is room for optimization in max function