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
            while nums[i] == 2 and i < right:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            while nums[i] == 0 and i > left:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1
        print nums

if __name__ == '__main__':
    s = Solution()
    s.sortColors([1,2,0,1,2,0])

