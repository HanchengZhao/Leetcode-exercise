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
                dp[i+1] = 9 * dp[i] # count as single digit
                if s[i-1] == '1':
                    dp[i+1] = (dp[i+1] + dp[i-1] * 9) % m # count as single digit from 1-9 or 11 to 19
                elif s[i-1] == '2':
                    dp[i+1] = (dp[i+1] + dp[i-1] * 6) % m
                elif s[i-1] == "*": # '**'
                    dp[i+1] = (dp[i+1] + dp[i-1] * 15) % m
            else:
                dp[i+1] = dp[i] if s[i] != '0' else 0
                if s[i-1] == '1':
                    dp[i+1] = (dp[i+1] + dp[i-1]) % m
                elif s[i-1] == '2' and int(s[i]) <= 6:
                    dp[i+1] = (dp[i+1] + dp[i-1]) % m
                elif s[i-1] == '*':
                    if int(s[i]) <= 6:
                        dp[i+1] = (dp[i+1] + 2 * dp[i-1]) % m
                    else:
                        dp[i+1] = (dp[i+1] + dp[i-1]) % m
        return dp[-1]

'''
check the current digit is '*' or not,
if it is,count the comb when * is one digit, which is 9
check the i-1 string, check if it is '1','2' or '*';
do the same thing for other case

'''