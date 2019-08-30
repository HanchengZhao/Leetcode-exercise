from collections import defaultdict


class WordDistance:

    def __init__(self, words: List[str]):
        self.dic = defaultdict(list)
        for i, val in enumerate(words):
            self.dic[val].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        shortest = float("inf")
        l1 = self.dic[word1]
        l2 = self.dic[word2]
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            shortest = min(shortest, abs(l1[i]-l2[j]))
            if l1[i] <= l2[j]:
                i += 1
            else:
                j += 1
        return shortest
