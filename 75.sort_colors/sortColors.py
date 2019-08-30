class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        left, i, right = 0, 0, n-1
        while i <= right:
            if nums[i] == 0:
                nums[i] = nums[left]
                nums[left] = 0
                left += 1
                i += 1 # remember to move forword
            elif nums[i] == 2:
                nums[i] = nums[right]
                nums[right] = 2
                right -= 1
            else:
                i += 1
        print nums

if __name__ == '__main__':
    s = Solution()
    s.sortColors([1,2,0,1,2,0])

