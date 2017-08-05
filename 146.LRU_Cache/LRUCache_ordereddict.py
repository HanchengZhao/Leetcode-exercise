from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = OrderedDict()



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.cache.pop(key, None)
        if val == None:
            return -1
        self.cache[key] = val
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cache.pop(key, None) == None and len(self.cache) == self.cap:
            self.cache.popitem(last = False)
        self.cache[key] = value