class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1 or s == t: # equal or have more than 1 difference
            return False
        if len(s) >= len(t):
            longer = s
            shorter = t
        else:
            longer = t
            shorter = s
        if len(longer) == len(shorter):
            dif = 0
            for i in xrange(len(longer)):
                if longer[i] != shorter[i]:
                    dif += 1
            return dif == 1
        else:
            i, j = 0, 0
            dif = 0
            while i < len(longer) and j < len(shorter):
                if longer[i] != shorter[j]:
                    dif += 1
                    i += 1
                else:
                    i += 1
                    j +=1
            return dif == 1 or j == len(shorter)