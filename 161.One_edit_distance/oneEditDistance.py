class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in xrange(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t): # if they are equal, this char should be replaced
                    return s[i+1:] == t[i+1:]
                elif len(s) > len(t): # if s is longer, the only possibility is deleting one char from s
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
        return abs(len(s) - len(t)) == 1 # check if there is only 1 difference left in the end