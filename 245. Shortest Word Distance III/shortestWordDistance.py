class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            indexes = [i for i, val in enumerate(words) if val == word1]
            shortest = len(words)
            for i, val in enumerate(indexes):
                if i > 0:
                    shortest = min(shortest, val - indexes[i-1])
            return shortest
        # normal way
        w1, w2 = -1, -1
        shortest = len(words)
        for i, val in enumerate(words):
            if val == word1:
                w1 = i
            if val == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                shortest = min(shortest, abs(w1 - w2))
        return shortest
