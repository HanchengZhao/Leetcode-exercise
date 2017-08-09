from collections import deque
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k >= len(nums):
            return max(nums) - min(nums) <= t
        firstK = nums[:k+1]
        window = deque(nums[:k+1])
        Min = min(firstK)
        Max = max(firstK)
        if Max - Min > t:
            return False
        for i in xrange(k+1,len(nums)):
            window.popleft()
            Max = Max(window)
            Min = Min(window)
            window.append(nums[i])

            Max = max(Max, nums[i])
            Min = min(Min, nums[i])
            if Max - Min > t:
                return False
        return True
