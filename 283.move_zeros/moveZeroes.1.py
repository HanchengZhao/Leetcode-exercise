class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        front = 0
        back = len(nums)-1
        while front < back:
            while nums[back] == 0:
                back -= 1
            while nums[front] != 0:
                front += 1
            if front < back:
                middle = nums[front]
                nums[front] = nums[back]
                nums[back] = middle
                front += 1
                back -= 1
        print nums
s = Solution()
print s.moveZeroes([1,0,3,5,6,0,5])
# didn't keep relative order