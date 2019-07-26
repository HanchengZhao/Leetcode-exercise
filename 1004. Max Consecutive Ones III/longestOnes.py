class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        longest = 0
        zeros = 0
        for i, val in enumerate(A):
            if val == 0:
                zeros += 1
                while zeros > K:
                    if A[l] == 0:
                        zeros -= 1
                    l += 1
            longest = max(longest, i - l + 1)
        return longest
