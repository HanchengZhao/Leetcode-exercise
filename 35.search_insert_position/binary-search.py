class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.binarySearch(nums, target, 0)

    def binarySearch(self, nums, target, startIndex):
        # print nums, startIndex
        if len(nums) == 0:
            return startIndex
        mid = (len(nums)-1) / 2
        if nums[mid] == target:
            return startIndex+mid
        if nums[mid] < target:
            return self.binarySearch(nums[mid+1:], target, startIndex+mid+1)
        if nums[mid] > target:
            return self.binarySearch(nums[:mid], target, startIndex)

if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1,2,3,4,5,6], 2)