from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        existed = set()
        queue = deque()
        queue.append(beginWord)
        existed.add(beginWord)
        length = 1
        while queue:
            size = len(queue)
            while size:
                word = queue.popleft()
                if word == endWord:
                    return length
                for i in xrange(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        string = word[:i] + char + word[i+1:]
                        if string in wordList and string not in existed:
                            queue.append(string)
                            existed.add(string)
                size -= 1
            length += 1
        #no match
        return 0
