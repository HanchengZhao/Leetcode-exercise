'''
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
'''
from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = deque(v1)
        self.v2 = deque(v2)
        self.signal = 1


    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            if self.signal == 1 and self.v1:
                if self.v2: self.signal = 0
                return self.v1.popleft()
            else:#v2
                self.signal = 1
                return self.v2.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.v1 or self.v2:
            return True
        else:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
v1, v2 = [1, 2],[3, 4, 5, 6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())
print v