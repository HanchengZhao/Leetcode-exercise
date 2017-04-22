class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = ''.join(S.split("-"))
        if not res:
            return ""
        count, i = 1, len(res)-1
        #start from the end
        while i:
            if count < K:
                count +=1
            else:
                res = res[:i] + "-" + res[i:]
                count = 1
            i -= 1
        return res.upper()
s = Solution()
print s.licenseKeyFormatting("---",4)