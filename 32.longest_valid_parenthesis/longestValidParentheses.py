class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        dp = [0] * len(s)
        for i in xrange(1, len(s)):
            # situation as '...()'
            if s[i] == ")" and s[i-1] == "(":
                dp[i] = 2 + dp[i-2] if i >=2 else 2
            # situation as '...))'
            elif s[i] == ")" and i-dp[i-1] > 0 and s[i-dp[i-1]-1] == "(":
                dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2] if (i - dp[i - 1]) >= 2 else dp[i-1] + 2
            longest = max(longest, dp[i])
        return longest
s = Solution()
print s.longestValidParentheses(")()())")