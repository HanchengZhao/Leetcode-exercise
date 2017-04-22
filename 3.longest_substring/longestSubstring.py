class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        norepeat = {}
        longest = 0
        slow = 0
        for fast in xrange(len(s)):
            if s[fast] in norepeat and norepeat[s[fast]] >= slow:
                slow = norepeat[s[fast]]+1
            else:
                longest = max(longest,fast-slow+1)
            norepeat[s[fast]] = fast
        return longest
s = Solution()
print s.lengthOfLongestSubstring("tmmzuxt")