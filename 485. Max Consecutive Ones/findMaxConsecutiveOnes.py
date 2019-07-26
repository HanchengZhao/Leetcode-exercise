class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        onelengths = 0
        for i in nums:
            if i == 1:
                onelengths += 1
                longest = max(longest, onelengths)
            else:
                onelengths = 0
        return longest
