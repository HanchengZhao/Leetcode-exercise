class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        stack = []
        i = 0
        digit = ""
        while i < len(s):
            if s[i].isdigit():
                digit += s[i]
                i += 1
            elif s[i] == "[":
                stack.append([int(digit), i, len(digit)]) # save multiple times, index and digit string length
                i += 1
                digit = ""
            elif s[i] == "]":
                last = stack.pop()
                s = s[:(last[1]-last[2])] + last[0] * s[(last[1]+1) : i] + s[(i+1):]
                i += last[0] * (i-last[1]-1) - (i-last[1]+last[2])
            else:
                i += 1
        return s
s = Solution()
print s.decodeString("3[a]2[bc]")
