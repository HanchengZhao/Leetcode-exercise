# class TrieNode(object):
#     def __init__(self, val):
#         self.sum = 0
#         self.val = val
#         self.children = {}

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key] = val
        # root = self.root
        # if key not in self.visited:
        #     for char in key:
        #         if char in root.children:
        #             root.children[char].val += val
        #         else:
        #             root.children[char] = TrieNode(val)
        #         root = root.children[char]


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        n = len(prefix)
        for i in self.dic.keys():
            if i[:n] == prefix:
                total += self.dic[i]
        return total
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)