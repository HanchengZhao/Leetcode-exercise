class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.s = nestedList[:]

    def next(self):
        """
        :rtype: int
        """
        return self.s.pop(0).getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.s and not self.s[0].isInteger(): # while s is not empty and the first element is not integer, it must be a list
            self.s = self.s.pop(0).getList() + self.s # pop the list out and add to the beginning of self.s
        if self.s and self.s[0].isInteger():
            return True
        return False