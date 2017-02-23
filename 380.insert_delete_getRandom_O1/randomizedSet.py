import random
class RandomizedSet(object):
    #use list to store the value, and use hashtable to keep track of the position
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.vals.append(val)
            self.pos[val] = len(self.vals)-1
            return True
        else:
            return False
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            #exchange the positon of val and last element, then pop
            last, index = self.vals[-1], self.pos[val]
            self.pos[last], self.vals[index] = index, last
            self.vals.pop(); self.pos.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.vals[random.randint(0, len(self.vals)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()