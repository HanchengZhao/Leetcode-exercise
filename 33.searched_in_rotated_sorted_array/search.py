class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums)-1

        while left<=right:
            mid = left+(right-left)/2
            lv, mv, rv = nums[left], nums[mid], nums[right]

            if lv<target<mv or mv<lv<target or target<mv<rv:
                right = mid-1
            elif lv<mv<target or target<rv<mv or mv<target<rv:
                left = mid+1
            else:
                break

        return left if target==lv else mid if target==mv else right if target==rv else -1