class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for i in xrange(m+1)]
        for i in strs:
            zeros = i.count("0")
            ones = i.count("1")
            for z in xrange(m, zeros-1, -1):
                for o in xrange(n, ones-1, -1):
                    # add this string to subset or not
                    dp[z][o] = max(dp[z - zeros][o - ones] + 1, dp[z][o])
        return dp[m][n]
s = Solution()
print s.findMaxForm(["10","1", "0"], 1, 1)