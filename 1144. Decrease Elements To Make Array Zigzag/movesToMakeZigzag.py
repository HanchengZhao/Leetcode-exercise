class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        odd_min = 0
        even_min = 0
        for i, val in enumerate(nums):
            if i % 2 == 1:
                left = nums[i-1] if i > 0 else 1001
                right = nums[i+1] if i < len(nums) - 1 else 1001
                if val >= min(left, right):
                    odd_min += val - min(left, right) + 1
            if i % 2 == 0:
                left = nums[i-1] if i > 0 else 1001
                right = nums[i+1] if i < len(nums) - 1 else 1001
                if val >= min(left, right):
                    even_min += val - min(left, right) + 1
        return min(odd_min, even_min)


s = Solution()
print(s.movesToMakeZigzag([10, 4, 4, 10, 10, 6, 2, 3]))

# [10, 4, 4, 10, 10, 6, 2, 3]
