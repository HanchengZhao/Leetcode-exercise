class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {}
        def can(s):
            if s not in memo:
                for i in xrange(len(s)-1):
                    if s[i:i+2] == "++" and not can(s[:i] + "--" + s[i+2:]):
                        memo[s] = True
                memo[s] = False
            return memo[s]
        return can(s)