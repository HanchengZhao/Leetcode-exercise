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
        if len(s) <= 1:
            return True
        i = 0
        j = len(s) -1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isPalindronme(s[i:j]) or isPalindronme(s[i+1:j+1])
        return True
s = Solution()
print s.validPalindrome("ebcbbececabbacecbbcbe")