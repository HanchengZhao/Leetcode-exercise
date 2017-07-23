class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        self.hash = {}
        for i in xrange(len(s)):
            for j in xrange(i+1, len(s)+1):
                if s[i:j] in self.hash:
                    count += 1
                elif self.isPalindrome(s[i:j]):
                    count += 1
        return count
        
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        self.hash[s] = 1
        return True
s= Solution()
print s.countSubstrings("aaaaaaa")