from collections import defaultdict


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        dic = defaultdict(list)
        for i, val in enumerate(words):
            dic[val].append(i)
        return min([abs(i-j) for i in dic[word1] for j in dic[word2]])
