class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        http://www.cnblogs.com/grandyang/p/4084408.html
        there are many cases that need to be considered:
        1. space ' ': can only exist at the beginning or the end
        2. dot '.': can only appear once, but it can be at front (".3") or middle(1.e2)
            or end('1.'), but it can not be after 'e/E, like 2e.1(false), 1e1.1(false)
            When it is at the end, the char before it should be digit, like "1."(true),
            "-."(false)
        3. 'e/E': it must have digits before or after it, and '.' can not be after it
        4. '-/+': it can only be at the begining or right after 'e', like "+1.e+5" true
        '''
        num = False
        numAfterE = True
        dot = False
        exp = False
        sign = False
        s = s.strip() # remove spaces for both end
        for i in xrange(len(s)):
            if s[i] == ' ':
                return False # no space in the midlle
            elif s[i] == '+' or s[i] == '-':
                if i > 0 and s[i-1] != 'e': # if not after 'e'
                    return False
                sign = True
            elif s[i].isdigit():
                num = True
                numAfterE = True
            elif s[i] == '.':
                if dot or exp: # '.' or e appeard before
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or not num: # e appeared before or no number before it
                    return False
                exp = True
                numAfterE = False
            else:
                return False # orthe char
        return num and numAfterE
s = Solution()
# print s.isNumber('.1')
print s.isNumber('1 ')
        
        
        
        
        
        
'''
# python trick
try:
    float(s)
    return True
except:
    return False
'''