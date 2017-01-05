import math
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1) #center is between two char
            str_len = max(len1,len2)
            if(str_len > (end - start)):
                end = i + math.floor(str_len / 2)
                start = i - math.floor(str_len-1 / 2)
        return s[int(start):int(end+1)]

    def expandAroundCenter(self, s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1
s = Solution()
print s.longestPalindrome("babad")