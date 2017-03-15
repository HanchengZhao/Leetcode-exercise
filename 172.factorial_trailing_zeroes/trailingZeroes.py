class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
s = Solution()
print s.trailingZeroes(100)