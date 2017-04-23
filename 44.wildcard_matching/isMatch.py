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
            if p_cur < len(p) and p[p_cur] == "*":
                star = p_cur
                match = s_cur
                p_cur += 1
            elif star != -1:
                match += 1
                s_cur = match
                p_cur = star+1
            else:
                return False
        while p_cur < len(p) and p[p_cur] == "*":
            p_cur += 1
        if p_cur == len(p):
            return True
        else:
            return False


