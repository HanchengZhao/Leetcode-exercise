class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {s[0]:1}
        total = 0
        for i in xrange(1, len(s)):
            theother = '0' if s[i] == '1' else '1'
            if s[i] != s[i-1]:
                counts[s[i]] = 1
            else:
                counts[s[i]] += 1
            if theother in counts:
                if counts[s[i]] <= counts[theother]:
                    total += 1
        return total
s = Solution()
print s.countBinarySubstrings("10101")