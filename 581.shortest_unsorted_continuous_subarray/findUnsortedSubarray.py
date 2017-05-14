class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f, b = len(nums)-1, 0
        for front in xrange(len(nums)-1):
            if nums[front] > nums[front+1]:
                f = front
                break
        for back in xrange(len(nums)-1, 0,-1):
            if nums[back] < nums[back-1]:
                b = back
                break
        if f < b:
            Min = min(nums[f:b+1])
            Max = max(nums[f:b+1])
            for i in xrange(f, -1, -1):
                if nums[i] > Min:
                    f = i
                else:
                    break
            for i in xrange(b, len(nums)):
                if nums[i] < Max:
                    b = i
                else:
                    break
            return b - f + 1
        else:
            return 0