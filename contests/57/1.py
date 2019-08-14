
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        s = set()
        res = ''
        length = 0
        for word in words:
            if len(word) == 1:
                s.add(word)
                if length == 0:
                    res = word
                    length = 1
                continue
            if word[:-1] in s:
                s.add(word)
                if len(word) > length:
                    res = word
                    length = len(word)
        return res
    
           
s = Solution()
print s.longestWord(["w","wo","wor","worl", "world"])