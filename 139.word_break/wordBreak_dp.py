class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for end in xrange(1, len(s)+1):
            for start in xrange(0, end):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
                    break
        return dp[-1]
'''
dp[i] stands for whether subarray(0, i) can be segmented into words from the dictionary. 
So dp[0] means whether subarray(0, 0) (which is an empty string) can be segmented, and of course the answer is yes.
The default value for boolean array is false. Therefore we need to set f[0] to be true.
'''