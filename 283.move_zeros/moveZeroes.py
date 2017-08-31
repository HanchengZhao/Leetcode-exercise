class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        insertIndex = 0
        for i in nums:
            if i:
                nums[insertIndex] = i
                insertIndex += 1
        for j in xrange(insertIndex, len(nums)):
            nums[j] = 0
# this solution takes up to O(n) in time complexity and O(1) in space, but a little bit more than n, since it
# traverses the array and move 0s in the end

# the above solution still needs n array writes, then we can reduce the write operation by only swapping when a 
# non-zero element is found

#All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.
#All elements between the current and slow pointer are zeroes.
class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIndex = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIndex], nums[i] = nums[i], nums[lastNonZeroIndex]
                lastNonZeroIndex += 1