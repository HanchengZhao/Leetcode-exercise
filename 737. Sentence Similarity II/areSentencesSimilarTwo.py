from collections import defaultdict


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        # use a bfs to find all similarities of word1 and check if w2 is in it
        def isSimilar(w1, w2, m):
            if w1 == w2:
                return True
            similar = m[w1]
            visited = set()
            while similar:
                if w2 in similar:
                    return True
                temp = []
                for s in similar:
                    if s in m and s not in visited:
                        temp += m[s]
                        visited.add(s)
                    similar = temp
            return False

        m = defaultdict(list)
        for a, b in pairs:
            m[a].append(b)
            m[b].append(a)
        for i in range(len(words1)):
            w1, w2 = words1[i], words2[i]
            if isSimilar(w1, w2, m):
                continue
            else:
                return False
        return True

# time : O(NP), n is maximum words of words1 and words2, P is length of pairs
