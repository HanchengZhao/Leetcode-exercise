class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            self.prefixsum[i] = self.prefixsum[i-1] + nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.prefixsum[j+1] - self.prefixsum[i]
