class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #build map
        dic = {}
        for word in wordDict:
            if word[0] in dic:
                dic[word[0]].append(word)
            else:
                dic[word[0]] = [word]
        #find sub
        return self.matchSub(dic, s, wordDict)
    def matchSub(self, dic, s, wordDict):
        if not s:
            return True
        if s[0] in dic:
            array = dic.get(s[0])
            for string in array:
                if string == s[:len(string)]:
                    if self.matchSub(dic,s[len(string):],wordDict):
                        return True
        return False
# the time complexity would be n^n