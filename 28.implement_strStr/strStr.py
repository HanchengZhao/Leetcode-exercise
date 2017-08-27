class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in xrange(len(haystack)-len(needle)+1): # has to plus 1 because we have to contain the first char of needle
            for j in xrange(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1
'''
use 2 pointers to check string match
'''
s = Solution()
print s.strStr('abcdefg','fg')