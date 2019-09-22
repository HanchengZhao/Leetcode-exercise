class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    # because the array is sorted, any k that's smaller than
                    # the current would satisfy the requirement
                    count += (k-j)
                    j += 1
                else:
                    k -= 1
        return count
