class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {} # store the count of all the chars
        targetcount = 0
        sourcecount = 0
        start = 0
        minlen = float("inf")
        minStr = ""
        for i in t:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            targetcount += 1
        # when loop through all the chars, subtract char's value if they are in the source
        # but only add source count when they are needed. When the count matches, narrow the 
        # window size by moving start pointer
        for i, val in enumerate(s):
            if val in dic:
                if dic[val] > 0: # means this char is needed
                    sourcecount += 1
                dic[val] -= 1  # this shoud be subtracted anyway
            while sourcecount == targetcount: # found all chars in s
                if minlen >= i - start + 1:
                    minlen = min(minlen, i - start + 1)
                    minStr = s[start: i + 1]
                if s[start] in dic:
                    dic[s[start]] += 1
                    if dic[s[start]] > 0:
                        sourcecount -= 1
                start += 1
        return minStr
                

s = Solution()
print s.minWindow("ADOBECODEBANC",
"ABC")