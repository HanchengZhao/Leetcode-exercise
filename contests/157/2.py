class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        needs = {}
        longest = 1
        for num in arr:
            if num in needs:
                prev = needs[num]
                longest = max(longest, prev + 1)
                needs[num+difference] = prev + 1
            else:
                needs[num+difference] = 1
        return longest
