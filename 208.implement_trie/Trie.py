class TreeNode(object):
    def __init__(self, val):
        self.children = dict() #key is char, value is node
        self.isWord = False
        self.val = val

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(0)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for letter in word:
            if not cur.children.get(letter):
                cur.children[letter] = TreeNode(letter)
            cur = cur.children[letter]
        cur.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for letter in word:
            cur = cur.children.get(letter)
            if not cur:
                return False
        return cur.isWord


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for letter in prefix:
            cur = cur.children.get(letter)
            if not cur:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)