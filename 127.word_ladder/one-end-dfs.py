from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord) or endWord not in wordList:
            return 0
        wordset = set(wordList)
        visited = set()
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for j in range(ord("a"), ord("z") + 1):
                    newWord = word[:i] + chr(j) + word[i+1:]
                    if newWord not in visited and newWord in wordset:
                        queue.append((newWord, step+1))
                        visited.add(word)
                        # this remove redundant operations
                        wordset.remove(newWord)