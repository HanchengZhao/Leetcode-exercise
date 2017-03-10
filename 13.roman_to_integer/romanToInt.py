class Solution(object):
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #last digit will be added anyway
        r = d[s[len(s)-1]]
        print r
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                r -= d[s[i]]
            else:
                r += d[s[i]]
        return r
