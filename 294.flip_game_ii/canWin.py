class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in xrange(len(s)-1):
            if s[i:i+2] == "++" and not self.canWin(s[:i] + "--" + s[i+2:]):
                return True
        return False
# TLE