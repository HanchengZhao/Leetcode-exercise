class Solution(object):
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        length = 0
        for n in nums:
            i, j = 0, length
            while i != j:
                m = (i + j) / 2
                if tails[m] < n:
                    i = m + 1
                else:
                    j = m
            tails[i] = n
            length = max(i + 1, length)
        return length
'''
(1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]

(1) is easy to understand, (2) is to always keep the minimum threshold
'''