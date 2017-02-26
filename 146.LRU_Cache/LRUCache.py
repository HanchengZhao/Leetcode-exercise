class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.queue = []
        self.dic = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.dic.get(key):
            self.queue.remove(key)
            self.queue.append(key) #renew the position
            return self.dic.get(key)
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.dic.get(key):
            self.queue.remove(key)
        elif len(self.queue) == self.cap:
            least = self.queue.pop(0)
            self.dic.pop(least)
        self.queue.append(key)
        self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# print obj.get(1)
# obj.put(1,1)
# obj.put(2,2)
# print obj.get(2)
# obj.put(3,3)
# print obj.get(1)
