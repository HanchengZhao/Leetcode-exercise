class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        n = len(nums)
        i = n - 2
        while i >= 0:
            # find a decreasing number from backwards
            if nums[i] >= nums[i+1]:
                i -= 1
            else:
                # traverse the rest elements until we find a number that's least larger-than nums[i] number
                j = i+1
                while j+1 < n and nums[j+1] > nums[i]:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
                # reverse the rest
                self.reverse(nums, i+1, n-1)
                return
        self.reverse(nums, 0, n-1)

    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


s = Solution()
s.nextPermutation([3, 2, 1])

''' 
The basic idea is to find the first decreasing number from behind, 
then find the smallest larger number behind it, swap them and reverse the array after this position

'''
