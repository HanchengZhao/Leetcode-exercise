class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        mask = 1
        for i in xrange(32):
            zeros = ones = 0
            for num in nums:
                if num & mask:  # not num & mask == 1
                    ones += 1
                else:
                    zeros += 1
            ans += ones * zeros
            mask <<= 1
        return ans
'''
only number of 1s and 0s on each bit matters, so we count ones and zeros,
add distance (ones * zeros) to the result
'''
                