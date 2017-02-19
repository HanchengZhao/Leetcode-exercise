class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for i in xrange(len(strs)-1):
            common = ""
            a,b = strs[i], strs[i+1]
            for j in xrange(min(len(a), len(b))):
                if a[j] == b[j]:
                    common += a[j]
                else: break
            prefix = common if len(common) < len(prefix) else prefix
        return prefix