'''
the ending situation can only be "P", "PL", "PLL"
'''
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n * 3
        m = 1000000007
        dp = [0] * (n+1)
        # i = 0, 1, 2 refers to 1, 2(P, L), 4(PL,LL,LP,PP)
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in xrange(3, n+1):
            dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % m
        res = dp[n]
        #insert A into any spot
        for j in xrange(1, n+1):
            res += dp[j-1] * dp[n-j] % m
        return res % m
s = Solution()
print s.checkRecord(100)