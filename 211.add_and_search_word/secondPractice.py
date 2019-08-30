class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.children = {}
    
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(0)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            if char not in cur.children: # not self.root.children
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.isWord = True
                
                
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(word, self.root)
    
    def find(self, word, node):
        if not word:
            return node.isWord # check if it the right ending
        first, rest = word[0], word[1:]
        if first != '.':
            return first in node.children and self.find(rest, node.children[first])
        else:
            return any(self.find(rest, child) for child in node.children.values())