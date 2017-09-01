class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 10**9 + 7
        if not s or s[0] == "0":
            return 0
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 9 if s[0] == "*" else 1
        for i in xrange(1, length):
            if s[i] == "*": # 1*
                if s[i-1] == '1':
                    dp[i+1] = (dp[i] * 9 + dp[i-1] * 9) % m # count as single digit from 1-9 or 11 to 19
                elif s[i-1] == '2':
                    dp[i+1] = (dp[i] * 9 + dp[i-1] * 6) % m
                elif s[i-1] == "*": # '**'
                    dp[i+1] = (dp[i] * 9 + dp[i-1] * 15) % m
                else: # other digit
                    dp[i+1] = (dp[i] * 9) % m
            elif s[i] == '0':
                if s[i-1] == '1' or '2':
                    dp[i+1] = (dp[i] + dp[i-1]) % m # count as single digit from 1-9 or 11 to 19
                elif s[i-1] == "*": # '*0' can only be 10 or 20
                    dp[i+1] = (dp[i-1] * 2) % m
                else: # has other digits before it
                    return 0
            elif s[i-1] == '*': # '*1'
                if int(s[i]) <= 6:
                    dp[i+1] = (dp[i] + dp[i-1] * 2) % m
                else:
                    dp[i+1] = dp[i]
            elif s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                dp[i+1] = dp[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]
        return dp[-1]