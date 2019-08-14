class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1
        n = len(nums)
        return self.quickSelect(nums, 0, n - 1, k)
    # select kth largest element
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left = start
        right = end
        pivot = nums[end] # choose the last num as pivot
        while left <= right:
            while left <= right and nums[left] > pivot: # put the bigger num on the left
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                # swap left and right
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # left == right here
        if start + k - 1 <= right: # on the larger part
            return self.quickSelect(nums, start, right, k)
        elif start + k - 1 >= left: # on the smaller part
            return self.quickSelect(nums, left, end, k - (left - start))
         # found k th number
        return nums[right + 1]
s = Solution()

print s.findKthLargest([3,2,1,5,6,4], 6)
print s.findKthLargest([99, 99], 1)
print s.findKthLargest([-1,2,0],1)