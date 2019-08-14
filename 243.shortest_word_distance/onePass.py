class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = -1，-1
        shortest = len(words)
        for w, i in enumerate(words):
            if w == word1:
                w1 = i
            if w == word2:
                w2 = i
            shortest = min(shortest, abs(w1 - w2))
        return shortest
s = Solution()
print s.shortestDistance(["a","c","b","a"],"a","b")