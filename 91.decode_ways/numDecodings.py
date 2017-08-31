class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        length = len(s)
        res = [0] * (length + 1) # memoization
        res[0] = res[1] = 1 # initialize
        for i in xrange(1, length):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2": # valid
                    res[i+1] = res[i-1]
                else: # not valid
                    return 0
            elif s[i-1] != "0" and int(s[i-1: i+1]) <= 26:
                res[i+1] = res[i-1] + res[i]
            else:# double digits not under 26, then only 1 option
                res[i+1] = res[i]
        return res[-1]
'''
The basic idea is dp, using an array to store all the previous combination numbers:
res[i+1] = res[i] + res[i-1] if (previous digits could be used) else res[i].

The trick part is dealing with 0, so if the digit before 0 is '1' or '2', count as
1 combination, the digit after 0 will only be considered as 1 combination
'''
