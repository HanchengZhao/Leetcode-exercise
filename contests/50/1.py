class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindronme(s):
            if len(s) <= 1:
                return True
            i = 0
            j = len(s) -1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        if isPalindronme(s):
            return True
        for i in xrange(len(s)):
            edit = s[:i]+s[i+1:]
            if isPalindronme(edit):
                return True
        return False
s = Solution()
print s.validPalindrome('abdyttda')