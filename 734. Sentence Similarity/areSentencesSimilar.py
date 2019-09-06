from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        m = defaultdict(set)
        for w1, w2 in pairs:
            m[w1].add(w2)
            m[w2].add(w1)
        for i in range(len(words1)):
            # either equal or in the set
            if words1[i] != words2[i] and words2[i] not in m[words1[i]]:
                return False
        return True

# time: O(n + p), n is number of words, p is number of pairs,
# space: O(p)
