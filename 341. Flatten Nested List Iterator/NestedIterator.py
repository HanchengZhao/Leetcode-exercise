# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList,0]] # keep the list and index

    def next(self):
        """
        :rtype: int
        """
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1 # increase the index
        return nestedList[i].getInteger() 

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList): # reach the end of list
                s.pop()
            else:
                x= nestedList[i]
                if x.isInteger(): # is integer
                    return True
                else: # is list
                    s[-1][1] += 1
                    s.append([x.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())