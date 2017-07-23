class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split(" ")
        for i, w in enumerate(words):
            shortest = len(w)
            for j in dict:
                l = len(j)
                if l < shortest:
                    if w[:l] == j:
                        words[i] = j
                        shortest = l
        return " ".join(words)
s = Solution()
print s.replaceWords(["cat", "bat", "rat"],"the cattle was rattled by the battery")