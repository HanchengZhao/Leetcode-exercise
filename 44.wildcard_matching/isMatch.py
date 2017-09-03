class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_cur, p_cur, match, star = 0, 0, 0, -1
        while s_cur < len(s):
            # match or "?"
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == "?"):
                s_cur += 1
                p_cur += 1
            # if "*"
            elif p_cur < len(p) and p[p_cur] == "*":
                star = p_cur
                match = s_cur
                p_cur += 1
            # if we do not have a match but have a "*" before it, we record the 
            # next char that is not '*', and find next match char in s
            elif star != -1:
                match += 1
                s_cur = match
                p_cur = star+1
            else:
                return False
        #if there are "***" at the end of pattern
        while p_cur < len(p) and p[p_cur] == "*":
            p_cur += 1
        #reach the end
        if p_cur == len(p):
            return True
        else:
            return False
'''
nots:
1. remember to check  p_cur < len(p) after adding p_cur
'''

'''Analysis:

For each element in s
If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
If not match, then we check if there is a * previously showed up,
       if there is no *,  return false;
       if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.

e.g.

abed
?b*d**

a=?, go on, b=b, go on,
e=*, save * position star=3, save s position ss = 3, p++
e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
d=d, go on, meet the end.
check the rest element in p, if all are *, true, else false;'''
