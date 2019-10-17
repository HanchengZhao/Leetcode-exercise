from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        layers = {}
        layers[beginWord] = [[beginWord]]
        wordSet = set(wordList)
        while layers:
            newLayers = defaultdict(list)
            for w in layers.keys():
                if w == endWord:
                    return layers[w]
                for i in range(len(w)):
                    for j in range(ord("a"), ord("z")+1):
                        newWord = w[:i] + chr(j) + w[i+1:]
                        if newWord in wordSet:
                            newLayers[newWord] += [l + [newWord] for l in layers[w]]
            layers = newLayers
            # avoid loops
            wordSet -= set(layers.keys())
        return []
'''
bfs, record each path that ends on the current word
'''
