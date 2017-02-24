class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        seperate = s.split(" ")
        rev = []
        for i in seperate:
            if i:
                rev.insert(0,i)
        return " ".join(rev)

s = Solution()
print s.reverseWords("the sky is   blue")