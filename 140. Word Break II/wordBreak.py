class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.dict = {}
        return self.helper(s, wordDict, 0)

    def helper(self, s, wordDict, start):
        if start in self.dict:
            return self.dict[start]
        res = []
        if start == len(s):
            res.append("")
        for end in xrange(start+1, len(s)+1):
            if s[start : end] in wordDict:
                lst = self.helper(s, wordDict, end)
                for l in lst:
                    space = "" if l == "" else " " 
                    res.append(s[start:end] + space + l)
        self.dict[start] = res
        return res
'''
the key used is the starting index of the string currently considered and the 
value contains all the sentences which can be formed using the substring from this starting index onwards. 
Thus, if we encounter the same starting index from different function calls, 
we can return the result directly from the hashmap rather than going for redundant function calls.

'''