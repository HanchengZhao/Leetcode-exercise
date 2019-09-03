class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        # n & (-n) here will detect the rightmost 1
        return n & (-n) == n
