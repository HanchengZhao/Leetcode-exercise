class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = []

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dic += dict

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in self.dic:
            if self.isOneCharDif(word, i):
                return True
        return False

    def isOneCharDif(self, w1, w2):
        if len(w1) != len(w2):
            return False
        for i in xrange(len(w1)):
            if w1[i] != w2[i]:
                return w1[i+1:] == w2[i+1:]
        return False # exact same
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)