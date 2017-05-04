class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1, i2 = [], [] #index list
        for i, val in enumerate(words):
            if val == word1:
                i1.append(i)
            elif val == word2:
                i2.append(i)
        i, j = 0, 0
        shortest = len(words)
        while i < len(i1) and j < len(i2):
            if i1[i] < i2[j]:
                shortest = min(i2[j]-i1[i], shortest)
                i += 1
            else:
                shortest = min(i1[i]-i2[j], shortest)
                j += 1
        return shortest