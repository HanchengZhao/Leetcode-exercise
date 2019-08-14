class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        self.root = TreeNode(0)

    def addWord(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TreeNode(char)
            cur = cur.children[char] # skip the existed char
        cur.isWord = True
    
    def search(self, word):
        def find(word, node):
            if not word:
                return node.isWord
            char, word = word[0], word[1:] # first char and the rest 
            if char != '.':
                return char in node.children and find(word, node.children[char])
            return any(find(word, kid) for kid in node.children.values())
        return find(word, self.root)
'''
A trie structure. In search, the idea is to use find function to skip a level if the char is '.'
'''