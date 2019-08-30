class Solution:
    def removeElement(self, nums, val: int) -> int:
        i, j = 0, len(nums)-1
        count = 0
        while i <= j:
            # last index that the num is not val
            while i <= j and nums[j] == val:
                count += 1
                j -= 1
            if i > j:
                break
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
                j -= 1
            i += 1
        return len(nums) - count
