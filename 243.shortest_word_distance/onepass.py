
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        w1, w2 = -1, -1
        Min = len(words)
        for i, val in enumerate(words):
            if val == word1:
                w1 = i
            if val == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                Min = min(Min, abs(w1 - w2))
        return Min
